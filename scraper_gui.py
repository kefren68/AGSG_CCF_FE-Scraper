#!/usr/bin/env python3
"""
AGSG CCF FE Scraper — GUI launcher
Requires only Python 3 standard library + requests (pip install requests)
"""

import sys
import os
import json
import base64

# Ensure the folder containing this script is always on sys.path so that
# "import scraper" works regardless of the current working directory
# (e.g. when launched via double-click on Windows).
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import threading
import queue
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

# ---------------------------------------------------------------------------
# Config persistence (saved next to this script as scraper_gui.cfg)
# Password is obfuscated with base64 — NOT encrypted, just not plain-text.
# ---------------------------------------------------------------------------
CONFIG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "scraper_gui.cfg")

def load_config():
    try:
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (OSError, json.JSONDecodeError):
        return {}

def save_config(data):
    try:
        with open(CONFIG_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
    except OSError:
        pass

CHECKBOX_KEYS = ("boxart", "videos", "gamelist", "bezels", "manuals",
                 "marquees", "3dboxes", "screenshots", "overwrite", "verbose",
                 "notfound_cache")

def encode_password(pw):
    return base64.b64encode(pw.encode()).decode() if pw else ""

def decode_password(enc):
    try:
        return base64.b64decode(enc.encode()).decode() if enc else ""
    except Exception:
        return ""


# ---------------------------------------------------------------------------
# Redirect stdout/stderr into a queue so the worker thread can send
# log lines to the GUI safely.
# ---------------------------------------------------------------------------
class QueueWriter:
    def __init__(self, q):
        self.q = q
    def write(self, text):
        if text:
            self.q.put(text)
    def flush(self):
        pass


# ---------------------------------------------------------------------------
# Remote folder browser dialog  (used in SSH mode)
# ---------------------------------------------------------------------------
class RemoteBrowserDialog(tk.Toplevel):
    """Simple dialog to navigate and select a directory on a remote device via SFTP."""

    def __init__(self, parent, sftp_ctx, initial_path="/"):
        super().__init__(parent)
        self.title("Browse Remote Folder")
        self.resizable(True, True)
        self.geometry("520x380")
        self._sftp     = sftp_ctx
        self._current  = initial_path.rstrip("/") or "/"
        self.result    = None
        self._build()
        self._list_dir(self._current)
        self.transient(parent)
        self.grab_set()
        parent.wait_window(self)

    def _build(self):
        frm_top = ttk.Frame(self)
        frm_top.pack(fill="x", padx=8, pady=(8, 2))
        ttk.Label(frm_top, text="Path:").pack(side="left")
        self.var_path = tk.StringVar()
        ttk.Entry(frm_top, textvariable=self.var_path,
                  state="readonly", width=48).pack(side="left", padx=4)

        frm_list = ttk.Frame(self)
        frm_list.pack(fill="both", expand=True, padx=8, pady=4)
        self._lb = tk.Listbox(frm_list, selectmode="single", font=("Monospace", 9))
        sb = ttk.Scrollbar(frm_list, command=self._lb.yview)
        self._lb.configure(yscrollcommand=sb.set)
        sb.pack(side="right", fill="y")
        self._lb.pack(fill="both", expand=True)
        self._lb.bind("<Double-Button-1>", lambda _e: self._enter())

        frm_btn = ttk.Frame(self)
        frm_btn.pack(fill="x", padx=8, pady=(2, 8))
        ttk.Button(frm_btn, text="↑ Parent",           command=self._go_parent).pack(side="left", padx=(0, 4))
        ttk.Button(frm_btn, text="✓ Select this folder", command=self._select ).pack(side="left")
        ttk.Button(frm_btn, text="Cancel",             command=self.destroy  ).pack(side="right")

    def _list_dir(self, path):
        import stat as _st
        self._current = path
        self.var_path.set(path)
        self._lb.delete(0, "end")
        try:
            attrs = self._sftp._sftp.listdir_attr(path)
        except Exception as e:
            self._lb.insert("end", f"[Error: {e}]")
            return
        dirs = sorted(
            a.filename for a in attrs
            if _st.S_ISDIR(a.st_mode or 0) and not a.filename.startswith(".")
        )
        for d in dirs:
            self._lb.insert("end", d)

    def _enter(self):
        sel = self._lb.curselection()
        if not sel:
            return
        name = self._lb.get(sel[0])
        if name.startswith("["):
            return
        new_path = self._current.rstrip("/") + "/" + name
        self._list_dir(new_path)

    def _go_parent(self):
        import posixpath
        parent = posixpath.dirname(self._current.rstrip("/")) or "/"
        self._list_dir(parent)

    def _select(self):
        self.result = self._current
        self.destroy()


# ---------------------------------------------------------------------------
# Main GUI
# ---------------------------------------------------------------------------
class ScraperGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("AGSG CCF FE Scraper")
        self.resizable(True, True)
        self.minsize(820, 520)
        self.geometry("1200x740")
        self._log_queue       = queue.Queue()
        self._worker          = None
        self._cfg             = load_config()
        self._ss_display_to_id = {}  # display string → ScreenScraper system_id
        self._ext_vars        = {}  # ext string → BooleanVar (checkboxes)
        self._sftp_conn       = None  # SFTPContext kept alive for remote browsing
        self._build_ui()
        self.var_dir.trace_add("write", lambda *_: self._refresh_folders())
        self.var_sys_override.trace_add("write", lambda *_: self._refresh_extensions())
        self.var_folder.trace_add("write", lambda *_: self._auto_detect_system())
        self._load_fields()
        self._poll_log()
        # Fetch full ScreenScraper system list in background
        threading.Thread(target=self._fetch_systems_async, daemon=True).start()

    # ------------------------------------------------------------------ UI --

    def _build_ui(self):
        PAD = {"padx": 6, "pady": 2}

        # Two-column layout: controls on the left, log on the right
        _outer = ttk.Frame(self)
        _outer.pack(fill="both", expand=True)
        frm_left = ttk.Frame(_outer)
        frm_left.pack(side="left", fill="y")
        ttk.Separator(_outer, orient="vertical").pack(side="left", fill="y", padx=3)
        _frm_right = ttk.LabelFrame(_outer, text="Log")
        _frm_right.pack(side="left", fill="both", expand=True, padx=(0, 8), pady=8)
        self.log_text = tk.Text(_frm_right, state="disabled",
                                bg="#1e1e1e", fg="#d4d4d4",
                                font=("Monospace", 9), relief="flat")
        _log_scroll = ttk.Scrollbar(_frm_right, command=self.log_text.yview)
        self.log_text.configure(yscrollcommand=_log_scroll.set)
        _log_scroll.pack(side="right", fill="y")
        self.log_text.pack(fill="both", expand=True, padx=2, pady=2)

        # ---- Games directory ----
        frm_dir = ttk.LabelFrame(frm_left, text="Games folder (SD card)")
        frm_dir.pack(fill="x", padx=10, pady=(6, 2))

        self.var_dir = tk.StringVar()
        ttk.Entry(frm_dir, textvariable=self.var_dir, width=52).pack(
            side="left", padx=(6, 2), pady=3)
        self._btn_browse = ttk.Button(frm_dir, text="Browse…", command=self._browse)
        self._btn_browse.pack(side="left", padx=(0, 6), pady=3)

        # ---- Credentials ----
        frm_cred = ttk.LabelFrame(frm_left, text="ScreenScraper account")
        frm_cred.pack(fill="x", padx=10, pady=2)

        # Left column: Username / Password
        ttk.Label(frm_cred, text="Username:").grid(row=0, column=0, sticky="e", **PAD)
        self.var_user = tk.StringVar()
        ttk.Entry(frm_cred, textvariable=self.var_user, width=28).grid(
            row=0, column=1, sticky="w", **PAD)

        ttk.Label(frm_cred, text="Password:").grid(row=1, column=0, sticky="e", **PAD)
        self.var_pass = tk.StringVar()
        ttk.Entry(frm_cred, textvariable=self.var_pass, show="•", width=28).grid(
            row=1, column=1, sticky="w", **PAD)

        # Separator between the two pairs
        ttk.Separator(frm_cred, orient="vertical").grid(
            row=0, column=2, rowspan=2, sticky="ns", padx=6)

        # Right column: Dev ID / Dev Password
        ttk.Label(frm_cred, text="Dev ID:").grid(row=0, column=3, sticky="e", **PAD)
        self.var_devid = tk.StringVar()
        self._e_devid = ttk.Entry(frm_cred, textvariable=self.var_devid, width=28,
                            foreground="gray")
        self._e_devid.insert(0, "optional – leave blank for default")
        self._e_devid.bind("<FocusIn>",  lambda e: self._clear_placeholder(self._e_devid, self.var_devid))
        self._e_devid.bind("<FocusOut>", lambda e: self._restore_placeholder(self._e_devid, self.var_devid,
                                                                        "optional – leave blank for default"))
        self._e_devid.grid(row=0, column=4, sticky="w", **PAD)

        ttk.Label(frm_cred, text="Dev Password:").grid(row=1, column=3, sticky="e", **PAD)
        self.var_devpass = tk.StringVar()
        self._e_devpass = ttk.Entry(frm_cred, textvariable=self.var_devpass, width=28,
                              foreground="gray")
        self._e_devpass.insert(0, "optional – leave blank for default")
        self._e_devpass.bind("<FocusIn>",  lambda e: self._clear_placeholder(self._e_devpass, self.var_devpass))
        self._e_devpass.bind("<FocusOut>", lambda e: self._restore_placeholder(self._e_devpass, self.var_devpass,
                                                                          "optional – leave blank for default"))
        self._e_devpass.grid(row=1, column=4, sticky="w", **PAD)

        # Bottom row: link + remember on the same line
        link = ttk.Label(frm_cred,
                         text="Use USERNAME (not email)  —  Register on screenscraper.fr",
                         foreground="#0066cc", cursor="hand2")
        link.grid(row=2, column=0, columnspan=3, sticky="w", padx=6, pady=(2, 4))
        link.bind("<Button-1>", lambda _: self._open_url(
            "https://www.screenscraper.fr/membreinscription.php"))

        self.var_remember = tk.BooleanVar(value=True)
        ttk.Checkbutton(frm_cred, text="Remember credentials",
                        variable=self.var_remember).grid(
            row=2, column=3, columnspan=2, sticky="w", padx=6, pady=(2, 4))

        # ---- Options ----
        frm_opt = ttk.LabelFrame(frm_left, text="Options")
        frm_opt.pack(fill="x", padx=10, pady=2)

        # What to download
        self.var_boxart      = tk.BooleanVar(value=True)
        self.var_videos      = tk.BooleanVar(value=True)
        self.var_bezels      = tk.BooleanVar(value=False)
        self.var_manuals     = tk.BooleanVar(value=False)
        self.var_marquees    = tk.BooleanVar(value=False)
        self.var_3dboxes     = tk.BooleanVar(value=False)
        self.var_screenshots = tk.BooleanVar(value=False)
        self.var_gamelist    = tk.BooleanVar(value=True)
        self.var_overwrite       = tk.BooleanVar(value=False)
        self.var_verbose         = tk.BooleanVar(value=False)
        self.var_notfound_cache  = tk.BooleanVar(value=False)

        _OP = {"padx": 6, "pady": 2}
        ttk.Checkbutton(frm_opt, text="Boxart",        variable=self.var_boxart     ).grid(row=0, column=0, sticky="w", **_OP)
        ttk.Checkbutton(frm_opt, text="Video snaps",   variable=self.var_videos     ).grid(row=0, column=1, sticky="w", **_OP)
        ttk.Checkbutton(frm_opt, text="Gamelist.xml",  variable=self.var_gamelist   ).grid(row=0, column=2, sticky="w", **_OP)
        ttk.Checkbutton(frm_opt, text="Bezels",        variable=self.var_bezels     ).grid(row=0, column=3, sticky="w", **_OP)
        ttk.Checkbutton(frm_opt, text="Marquees",      variable=self.var_marquees   ).grid(row=1, column=0, sticky="w", **_OP)
        ttk.Checkbutton(frm_opt, text="3D box art",    variable=self.var_3dboxes    ).grid(row=1, column=1, sticky="w", **_OP)
        ttk.Checkbutton(frm_opt, text="Screenshots",   variable=self.var_screenshots).grid(row=1, column=2, sticky="w", **_OP)
        ttk.Checkbutton(frm_opt, text="Manuals (PDF)", variable=self.var_manuals    ).grid(row=1, column=3, sticky="w", **_OP)
        ttk.Separator(frm_opt, orient="vertical").grid(row=0, column=4, rowspan=2, sticky="ns", padx=8)
        ttk.Checkbutton(frm_opt, text="Overwrite",     variable=self.var_overwrite  ).grid(row=0, column=5, sticky="w", **_OP)
        ttk.Checkbutton(frm_opt, text="Verbose log",   variable=self.var_verbose    ).grid(row=1, column=5, sticky="w", **_OP)
        ttk.Separator(frm_opt, orient="vertical").grid(row=0, column=6, rowspan=2, sticky="ns", padx=8)
        ttk.Checkbutton(frm_opt, text="Skip not found\n(save KO quota)",
                        variable=self.var_notfound_cache).grid(row=0, column=7, rowspan=2, sticky="w", **_OP)

        # ---- SSH (remote device) ----
        frm_ssh = ttk.LabelFrame(frm_left, text="SSH — scrape games folder on a remote device (optional)")
        frm_ssh.pack(fill="x", padx=10, pady=2)

        self.var_ssh_enabled = tk.BooleanVar(value=False)
        ttk.Checkbutton(frm_ssh, text="Enable SSH", variable=self.var_ssh_enabled,
                        command=self._toggle_ssh).grid(
            row=0, column=0, sticky="w", padx=6, pady=2)

        self._btn_ssh_connect = ttk.Button(frm_ssh, text="► Connect",
                                           command=self._ssh_connect, state="disabled")
        self._btn_ssh_connect.grid(row=0, column=1, sticky="w", padx=(0, 4), pady=2)
        self._btn_ssh_disconnect = ttk.Button(frm_ssh, text="■ Disconnect",
                                              command=self._ssh_disconnect, state="disabled")
        self._btn_ssh_disconnect.grid(row=0, column=2, sticky="w", padx=(0, 4), pady=2)
        self._lbl_ssh_status = ttk.Label(frm_ssh, text="● Not connected", foreground="#888888")
        self._lbl_ssh_status.grid(row=0, column=3, sticky="w", padx=4, pady=2)

        ttk.Label(frm_ssh, text="Host:").grid(row=1, column=0, sticky="e", **PAD)
        self.var_ssh_host = tk.StringVar()
        self._e_ssh_host = ttk.Entry(frm_ssh, textvariable=self.var_ssh_host, width=24, state="disabled")
        self._e_ssh_host.grid(row=1, column=1, sticky="w", **PAD)

        ttk.Label(frm_ssh, text="Port:").grid(row=1, column=2, sticky="e", **PAD)
        self.var_ssh_port = tk.StringVar(value="22")
        self._e_ssh_port = ttk.Entry(frm_ssh, textvariable=self.var_ssh_port, width=6, state="disabled")
        self._e_ssh_port.grid(row=1, column=3, sticky="w", **PAD)

        ttk.Label(frm_ssh, text="Username:").grid(row=2, column=0, sticky="e", **PAD)
        self.var_ssh_user = tk.StringVar(value="root")
        self._e_ssh_user = ttk.Entry(frm_ssh, textvariable=self.var_ssh_user, width=16, state="disabled")
        self._e_ssh_user.grid(row=2, column=1, sticky="w", **PAD)

        ttk.Label(frm_ssh, text="Key file:").grid(row=2, column=2, sticky="e", **PAD)
        self.var_ssh_keyfile = tk.StringVar()
        self._e_ssh_keyfile = ttk.Entry(frm_ssh, textvariable=self.var_ssh_keyfile,
                                        width=32, state="disabled")
        self._e_ssh_keyfile.grid(row=2, column=3, sticky="w", **PAD)
        self._btn_ssh_keyfile = ttk.Button(frm_ssh, text="Browse…", state="disabled",
                                           command=self._browse_keyfile)
        self._btn_ssh_keyfile.grid(row=2, column=4, sticky="w", **PAD)

        ttk.Label(frm_ssh,
            text="Authentication via SSH key only.  "
                 "After connecting, Browse… will navigate the remote device.",
            foreground="#666666").grid(row=3, column=0, columnspan=6, sticky="w", padx=6, pady=(0, 4))

        self._ssh_cred_widgets = [self._e_ssh_host, self._e_ssh_port,
                                  self._e_ssh_user,
                                  self._e_ssh_keyfile, self._btn_ssh_keyfile]

        # ---- Folder → System mapping ----
        frm_map = ttk.LabelFrame(frm_left, text="Folder → System  (for renamed folders)")
        frm_map.pack(fill="x", padx=10, pady=2)

        ttk.Label(frm_map, text="Folder:").grid(row=0, column=0, sticky="e", **PAD)
        self.var_folder = tk.StringVar(value="— all —")
        self._cb_folder = ttk.Combobox(frm_map, textvariable=self.var_folder,
                                       state="readonly", width=24)
        self._cb_folder["values"] = ["— all —"]
        self._cb_folder.current(0)
        self._cb_folder.grid(row=0, column=1, sticky="w", **PAD)

        ttk.Label(frm_map, text="ScreenScraper system:").grid(row=0, column=2, sticky="e", **PAD)
        self.var_sys_override = tk.StringVar(value="— auto —")
        self._cb_system = ttk.Combobox(frm_map, textvariable=self.var_sys_override,
                                       state="readonly", width=36)
        try:
            from screenscraper_extensions import SYSTEM_NAMES as _sn
            self._ss_display_to_id = {f"{name}  [{sid}]": sid for sid, name in _sn.items()}
            _sys_display = sorted(self._ss_display_to_id.keys())
        except ImportError:
            _sys_display = []
        self._all_systems = ["— auto —"] + _sys_display
        self._cb_system["values"] = self._all_systems
        self._cb_system.current(0)
        self._cb_system.grid(row=0, column=3, sticky="w", **PAD)

        ttk.Button(frm_map, text="↺", width=3,
                   command=self._refresh_folders).grid(row=0, column=4, padx=(2, 6))

        # ---- Extension filter ----
        frm_ext = ttk.LabelFrame(frm_left, text="ROM extensions to scan  (uncheck to exclude)")
        frm_ext.pack(fill="x", padx=10, pady=2)

        # Placeholder label shown when no system is selected
        self._ext_label = ttk.Label(frm_ext,
                                    text="Select a system above to see its extensions.",
                                    foreground="#888888")
        self._ext_label.pack(padx=8, pady=4)

        # Grid of checkboxes (populated dynamically)
        self._ext_inner = ttk.Frame(frm_ext)
        self._ext_inner.pack(fill="x", padx=4, pady=(0, 2))

        # All / None buttons (hidden until a system is selected)
        self._frm_ext_btns = ttk.Frame(frm_ext)
        ttk.Button(self._frm_ext_btns, text="All", width=5,
                   command=lambda: self._ext_select_all(True)).pack(side="left", padx=(0, 4))
        ttk.Button(self._frm_ext_btns, text="None", width=5,
                   command=lambda: self._ext_select_all(False)).pack(side="left")

        # ---- Start / Stop buttons ----
        frm_btn = ttk.Frame(frm_left)
        frm_btn.pack(fill="x", padx=10, pady=2)

        self.btn_start = ttk.Button(frm_btn, text="▶  Start scraping",
                                    command=self._start)
        self.btn_start.pack(side="left", padx=(0, 6))

        self.btn_stop = ttk.Button(frm_btn, text="■  Stop",
                                   command=self._stop, state="disabled")
        self.btn_stop.pack(side="left")

        self.lbl_status = ttk.Label(frm_btn, text="Ready.")
        self.lbl_status.pack(side="right")

        # ---- Progress bar ----
        self.progress = ttk.Progressbar(frm_left, mode="indeterminate")
        self.progress.pack(fill="x", padx=10, pady=(0, 2))

        # ---- Quota indicator ----
        frm_quota = ttk.Frame(frm_left)
        frm_quota.pack(fill="x", padx=10, pady=(0, 2))
        self.lbl_quota = ttk.Label(frm_quota, text="Daily quota: —",
                                   foreground="#888888")
        self.lbl_quota.pack(side="left")

    # ---------------------------------------------------------------- logic --

    _PLACEHOLDER = "optional – leave blank for default"

    def _load_fields(self):
        """Populate form fields from saved config."""
        cfg = self._cfg
        if cfg.get("games_dir"):
            self.var_dir.set(cfg["games_dir"])
        if cfg.get("user"):
            self.var_user.set(cfg["user"])
        if cfg.get("password_enc"):
            self.var_pass.set(decode_password(cfg["password_enc"]))
        if cfg.get("devid"):
            self._e_devid.config(foreground="black")
            self._e_devid.delete(0, "end")
            self._e_devid.insert(0, cfg["devid"])
        if cfg.get("devpass_enc"):
            decoded = decode_password(cfg["devpass_enc"])
            if decoded:
                self._e_devpass.config(foreground="black")
                self._e_devpass.delete(0, "end")
                self._e_devpass.insert(0, decoded)
        self.var_remember.set(cfg.get("remember", True))
        # Restore checkbox states
        for key in CHECKBOX_KEYS:
            val = cfg.get(f"opt_{key}")
            if val is not None:
                getattr(self, f"var_{key}").set(bool(val))
        # Restore folder/system mapping
        # First restore the folder selection (folder list refreshed via var_dir trace)
        if cfg.get("folder_map_folder"):
            fld_val = cfg["folder_map_folder"]
            if fld_val in list(self._cb_folder["values"]):
                self.var_folder.set(fld_val)
        else:
            self.var_folder.set("— all —")
        # Restore system: prefer folder_system_map (per-folder memory),
        # fall back to old folder_map_system/folder_map_system_id keys
        fld_val = self.var_folder.get()
        fsmap   = cfg.get("folder_system_map", {})
        if fld_val and fld_val != "— all —" and fld_val in fsmap:
            entry = fsmap[fld_val]
            disp  = entry.get("display", "")
            if disp in self._ss_display_to_id:
                self.var_sys_override.set(disp)
            elif entry.get("id"):
                for d, sid in self._ss_display_to_id.items():
                    if sid == entry["id"]:
                        self.var_sys_override.set(d)
                        break
        elif cfg.get("folder_map_system"):
            sys_val = cfg["folder_map_system"]
            if sys_val in list(self._cb_system["values"]):
                self.var_sys_override.set(sys_val)
            elif cfg.get("folder_map_system_id"):
                saved_id = cfg["folder_map_system_id"]
                for disp, sid in self._ss_display_to_id.items():
                    if sid == saved_id:
                        self.var_sys_override.set(disp)
                        break
        # Restore SSH settings
        if cfg.get("ssh_enabled"):
            self.var_ssh_enabled.set(True)
            self._toggle_ssh()
        self.var_ssh_host.set(cfg.get("ssh_host", ""))
        self.var_ssh_port.set(cfg.get("ssh_port", "22"))
        self.var_ssh_user.set(cfg.get("ssh_user", "root"))
        self.var_ssh_keyfile.set(cfg.get("ssh_keyfile", ""))

    def _save_fields(self):
        """Persist current form fields to config file."""
        if not self.var_remember.get():
            # Clear saved credentials if user unchecked "remember"
            save_config({})
            return
        devid = self.var_devid.get().strip()
        if devid == self._PLACEHOLDER:
            devid = ""
        devpass = self.var_devpass.get().strip()
        if devpass == self._PLACEHOLDER:
            devpass = ""
        folder_sel = self.var_folder.get()
        sys_sel    = self.var_sys_override.get()
        cfg = {
            "games_dir":         self.var_dir.get().strip(),
            "user":              self.var_user.get().strip(),
            "password_enc":      encode_password(self.var_pass.get()),
            "devid":             devid,
            "devpass_enc":       encode_password(devpass),
            "remember":          True,
        }
        # Persist folder→system map (remembers every folder's last chosen system)
        if folder_sel and folder_sel != "— all —" and sys_sel and sys_sel != "— auto —":
            fsmap = cfg.get("folder_system_map", {})
            if not isinstance(fsmap, dict):
                fsmap = {}
            fsmap[folder_sel] = {
                "display": sys_sel,
                "id":      self._ss_display_to_id.get(sys_sel),
            }
            cfg["folder_system_map"] = fsmap
        # Keep legacy single-pair keys for backwards compat
        cfg["folder_map_folder"]    = "" if folder_sel == "— all —"  else folder_sel
        cfg["folder_map_system"]    = "" if sys_sel    == "— auto —" else sys_sel
        cfg["folder_map_system_id"] = self._ss_display_to_id.get(sys_sel)
        # Persist checkbox states so they survive GUI restarts
        for key in CHECKBOX_KEYS:
            cfg[f"opt_{key}"] = getattr(self, f"var_{key}").get()
        # Persist extension selection per system_id (all systems remembered independently)
        if self._ext_vars:
            sid = self._ss_display_to_id.get(self.var_sys_override.get())
            if sid is not None:
                saved_map = cfg.get("ext_override", {})
                # migrate old single-system format
                if isinstance(saved_map, dict) and "system_id" in saved_map:
                    saved_map = {str(saved_map["system_id"]): saved_map.get("exts", [])}
                saved_map[str(sid)] = [ext for ext, var in self._ext_vars.items() if var.get()]
                cfg["ext_override"] = saved_map
        # Persist SSH settings
        cfg["ssh_enabled"]  = self.var_ssh_enabled.get()
        cfg["ssh_host"]     = self.var_ssh_host.get().strip()
        cfg["ssh_port"]     = self.var_ssh_port.get().strip() or "22"
        cfg["ssh_user"]     = self.var_ssh_user.get().strip()
        cfg["ssh_keyfile"]  = self.var_ssh_keyfile.get().strip()
        save_config(cfg)

    def _clear_placeholder(self, widget, var):
        if widget.get() == self._PLACEHOLDER:
            widget.config(foreground="black", show="")
            widget.delete(0, "end")

    def _restore_placeholder(self, widget, var, text):
        if not widget.get():
            widget.config(foreground="gray", show="")
            widget.insert(0, text)

    def _fetch_systems_async(self):
        """Background thread: build the full ScreenScraper system display list.
        Uses SYSTEM_NAMES from screenscraper_extensions (already populated at
        startup); no extra API call is needed just for the combobox."""
        try:
            from screenscraper_extensions import SYSTEM_NAMES as _sn
            display_to_id = {f"{name}  [{sid}]": sid for sid, name in _sn.items()}
            new_display   = sorted(display_to_id.keys())
        except ImportError:
            return
        if not new_display:
            return
        new_values = ["— auto —"] + new_display
        current    = self.var_sys_override.get()
        self._all_systems      = new_values
        self._ss_display_to_id = display_to_id
        self.after(0, lambda: self._apply_systems_list(new_values, current))

    def _auto_detect_system(self):
        """When a folder is selected, try to pick the best matching SS system."""
        folder = self.var_folder.get()
        if not folder or folder == "— all —":
            return

        # 0) User's explicit past choice for this folder takes top priority
        fsmap = self._cfg.get("folder_system_map", {})
        if folder in fsmap:
            entry = fsmap[folder]
            disp  = entry.get("display", "")
            if disp in self._ss_display_to_id:
                self.var_sys_override.set(disp)
                return
            saved_id = entry.get("id")
            if saved_id:
                for d, sid in self._ss_display_to_id.items():
                    if sid == saved_id:
                        self.var_sys_override.set(d)
                        return

        # Normalize helper
        import re as _re
        def _norm(s):
            return _re.sub(r"[^a-z0-9 ]", " ", s.lower()).split()

        folder_words = set(_norm(folder))

        # 1) Check against SYSTEM_IDS (hand-curated mapping in scraper.py)
        try:
            from scraper import SYSTEM_IDS
        except ImportError:
            SYSTEM_IDS = {}
        folder_key = " ".join(_norm(folder))
        if folder_key in SYSTEM_IDS:
            target_id = SYSTEM_IDS[folder_key]
            for disp, sid in self._ss_display_to_id.items():
                if sid == target_id:
                    self.var_sys_override.set(disp)
                    return

        # 2) Substring match: folder name contained in system name (or vice-versa)
        folder_str = " ".join(_norm(folder))
        best_disp  = None
        best_score = 0
        for disp, sid in self._ss_display_to_id.items():
            # Extract just the name part (drop " [id]" suffix)
            name_part  = disp.rsplit("  [", 1)[0]
            name_words = set(_norm(name_part))
            if not name_words:
                continue
            common = folder_words & name_words
            if not common:
                continue
            # Jaccard-style score weighted to prefer larger overlap
            score = len(common) / len(folder_words | name_words)
            # Bonus: all folder words are present in system name
            if folder_words <= name_words:
                score += 1
            if score > best_score:
                best_score = score
                best_disp  = disp

        # Only auto-select if there's a reasonably confident match
        if best_disp and best_score >= 0.3:
            self.var_sys_override.set(best_disp)

    def _apply_systems_list(self, values, current):
        self._cb_system["values"] = values
        if current in values:
            self.var_sys_override.set(current)
        else:
            self.var_sys_override.set("— auto —")

    def _refresh_extensions(self):
        """Rebuild the extension checkboxes whenever the system combobox changes."""
        # Clear existing checkboxes
        for w in self._ext_inner.winfo_children():
            w.destroy()
        self._ext_vars.clear()

        sys_sel = self.var_sys_override.get()
        if sys_sel == "— auto —" or sys_sel not in self._ss_display_to_id:
            self._frm_ext_btns.pack_forget()
            self._ext_label.config(
                text="Select a system above to see its extensions.",
                foreground="#888888")
            self._ext_label.pack(padx=8, pady=4)
            return

        sid = self._ss_display_to_id[sys_sel]
        try:
            from screenscraper_extensions import SYSTEM_EXTENSIONS
            exts = sorted(SYSTEM_EXTENSIONS.get(sid, []))
        except ImportError:
            exts = []

        if not exts:
            self._frm_ext_btns.pack_forget()
            self._ext_label.config(
                text="No extensions found for this system in the database.",
                foreground="#888888")
            self._ext_label.pack(padx=8, pady=4)
            return

        self._ext_label.pack_forget()

        # Restore saved extension state for this system (if any)
        saved_map = self._cfg.get("ext_override", {})
        # support old single-system format for backwards compat
        if isinstance(saved_map, dict) and "system_id" in saved_map:
            saved_map = {str(saved_map["system_id"]): saved_map.get("exts", [])}
        saved_set = None
        if str(sid) in saved_map:
            saved_set = set(saved_map[str(sid)])

        COLS = 8
        for i, ext in enumerate(exts):
            initial = True if saved_set is None else (ext in saved_set)
            var = tk.BooleanVar(value=initial)
            self._ext_vars[ext] = var
            cb = ttk.Checkbutton(self._ext_inner, text=f".{ext}", variable=var)
            cb.grid(row=i // COLS, column=i % COLS, sticky="w", padx=4, pady=1)

        self._frm_ext_btns.pack(anchor="w", padx=4, pady=(2, 4))

    def _ext_select_all(self, state: bool):
        """Check or uncheck all extension checkboxes."""
        for var in self._ext_vars.values():
            var.set(state)

    def _toggle_ssh(self):
        """Enable or disable SSH credential fields when the checkbox is toggled."""
        enabled = self.var_ssh_enabled.get()
        state   = "normal" if enabled else "disabled"
        for w in self._ssh_cred_widgets:
            w.config(state=state)
        self._btn_ssh_connect.config(state=state)
        self._btn_ssh_disconnect.config(state="disabled")
        self._btn_browse.config(state="normal")   # always enabled; _browse handles "not connected"
        if not enabled:
            self._ssh_disconnect()
            self._cb_folder["values"] = ["\u2014 all \u2014"]
            self.var_folder.set("\u2014 all \u2014")

    def _ssh_connect(self):
        """Establish the preview SFTP connection used for Browse."""
        host    = self.var_ssh_host.get().strip()
        port    = self.var_ssh_port.get().strip() or "22"
        user    = self.var_ssh_user.get().strip()
        keyfile = self.var_ssh_keyfile.get().strip() or None
        if not host or not user:
            messagebox.showerror("SSH", "Please enter Host and Username before connecting.")
            return
        self._lbl_ssh_status.config(text="● Connecting…", foreground="#cc7700")
        self.update_idletasks()
        try:
            import scraper
            self._sftp_conn = scraper.SFTPContext(
                host=host, port=int(port), username=user,
                key_filename=keyfile,
            )
            self._lbl_ssh_status.config(text=f"● Connected to {user}@{host}",
                                        foreground="#228b22")
            self._btn_ssh_connect.config(state="disabled")
            self._btn_ssh_disconnect.config(state="normal")
            self._btn_browse.config(state="normal")
            # Populate folder combobox with remote system dirs
            initial = self.var_dir.get().strip() or "/"
            dirs    = self._sftp_conn.list_subdirs(initial)
            vals    = ["\u2014 all \u2014"] + sorted(dirs)
            self._cb_folder["values"] = vals
        except Exception as e:
            self._lbl_ssh_status.config(text="● Connection failed", foreground="#cc0000")
            messagebox.showerror("SSH connection failed", str(e))
            self._sftp_conn = None

    def _ssh_disconnect(self):
        """Close the preview SFTP connection."""
        if self._sftp_conn:
            try:
                self._sftp_conn.close()
            except Exception:
                pass
            self._sftp_conn = None
        self._lbl_ssh_status.config(text="● Not connected", foreground="#888888")
        self._btn_ssh_connect.config(
            state="normal" if self.var_ssh_enabled.get() else "disabled")
        self._btn_ssh_disconnect.config(state="disabled")
        if self.var_ssh_enabled.get():
            self._btn_browse.config(state="disabled")

    def _browse_keyfile(self):
        """Open file chooser for the SSH private key file."""
        path = filedialog.askopenfilename(
            title="Select SSH private key file",
            filetypes=[("All files", "*"), ("PEM key", "*.pem"),
                       ("OpenSSH key", "id_rsa id_ed25519 id_ecdsa")])
        if path:
            self.var_ssh_keyfile.set(path)

    def _refresh_folders(self):
        """Populate the folder combobox with subdirectories of the Games folder."""
        if self.var_ssh_enabled.get():
            return  # folder listing handled by _ssh_connect / Browse
        games_dir = self.var_dir.get().strip()
        if not games_dir or not os.path.isdir(games_dir):
            self._cb_folder["values"] = ["— all —"]
            self.var_folder.set("— all —")
            return
        try:
            folders = sorted(
                d for d in os.listdir(games_dir)
                if os.path.isdir(os.path.join(games_dir, d)) and not d.startswith(".")
            )
        except OSError:
            folders = []
        current = self.var_folder.get()
        new_values = ["— all —"] + folders
        self._cb_folder["values"] = new_values
        if current not in new_values:
            self.var_folder.set("— all —")

    def _browse(self):
        if self.var_ssh_enabled.get():
            # SSH mode: open remote folder browser if connected
            if not self._sftp_conn:
                messagebox.showinfo("SSH", "Connect to the device first.")
                return
            current = self.var_dir.get().strip() or "/"
            dlg = RemoteBrowserDialog(self, self._sftp_conn, initial_path=current)
            if dlg.result:
                self.var_dir.set(dlg.result)
                # Refresh folder combo with sub-dirs of the selected path
                dirs = self._sftp_conn.list_subdirs(dlg.result)
                vals = ["\u2014 all \u2014"] + sorted(dirs)
                self._cb_folder["values"] = vals
            return
        path = filedialog.askdirectory(title="Select the Games folder on your SD card")
        if path:
            self.var_dir.set(path)

    def _open_url(self, url):
        import webbrowser
        webbrowser.open(url)

    def _start(self):
        games_dir = self.var_dir.get().strip()
        user      = self.var_user.get().strip()
        password  = self.var_pass.get()
        devid     = self.var_devid.get().strip()
        devpass   = self.var_devpass.get().strip()
        # treat placeholder text as empty
        if devid == self._PLACEHOLDER:
            devid = ""
        if devpass == self._PLACEHOLDER:
            devpass = ""
        devid   = devid   or None
        devpass = devpass or None

        if not games_dir:
            messagebox.showerror("Missing field", "Please select the Games folder.")
            return
        ssh_enabled = self.var_ssh_enabled.get()
        ssh_host    = self.var_ssh_host.get().strip()
        ssh_port    = self.var_ssh_port.get().strip() or "22"
        ssh_user    = self.var_ssh_user.get().strip()
        ssh_keyfile = self.var_ssh_keyfile.get().strip() or None
        if ssh_enabled:
            if not ssh_host:
                messagebox.showerror("SSH", "Please enter the SSH host.")
                return
            if not ssh_user:
                messagebox.showerror("SSH", "Please enter the SSH username.")
                return
        else:
            if not os.path.isdir(games_dir):
                messagebox.showerror("Invalid path", f"'{games_dir}' is not a valid directory.")
                return
        if not user:
            messagebox.showerror("Missing field", "Please enter your ScreenScraper username.")
            return
        if not password:
            messagebox.showerror("Missing field", "Please enter your ScreenScraper password.")
            return

        self.btn_start.config(state="disabled")
        self.btn_stop.config(state="normal")
        self.progress.start(12)
        self.lbl_status.config(text="Running…")
        self.lbl_quota.config(text="Daily quota: —", foreground="#888888")
        self._log_clear()
        self._save_fields()

        # Build args list for scraper.main() — redirect stdout/stderr to queue
        import argparse
        from pathlib import Path

        try:
            import scraper
        except ImportError:
            messagebox.showerror("Import error",
                "scraper.py not found.\nMake sure scraper.py is in the same folder as this file.")
            self._done()
            return

        # Folder → system mapping
        folder_sel = self.var_folder.get()
        sys_sel    = self.var_sys_override.get()
        if folder_sel and folder_sel != "— all —":
            opt_system = folder_sel
            if sys_sel and sys_sel != "— auto —":
                _sid = self._ss_display_to_id.get(sys_sel)
                folder_overrides = {folder_sel: _sid} if _sid else None
            else:
                folder_overrides = None
        else:
            opt_system = None
            folder_overrides = None

        # Collect selected extensions (None = use automatic SYSTEM_EXTENSIONS whitelist)
        if self._ext_vars:
            ext_override = {ext for ext, var in self._ext_vars.items() if var.get()}
            if not ext_override:
                messagebox.showerror("No extensions selected",
                                     "Please select at least one extension to scan.")
                return
        else:
            ext_override = None

        # Run scraper in a background thread
        self._stop_event = threading.Event()

        def worker():
            # Redirect stdout/stderr
            old_out, old_err = sys.stdout, sys.stderr
            sys.stdout = QueueWriter(self._log_queue)
            sys.stderr = QueueWriter(self._log_queue)
            sftp_ctx = None
            try:
                # SSH connection (if enabled)
                if ssh_enabled:
                    try:
                        sftp_ctx = scraper.SFTPContext(
                            host=ssh_host, port=int(ssh_port),
                            username=ssh_user,
                            key_filename=ssh_keyfile,
                        )
                        print(f"[SSH] Connected to {ssh_user}@{ssh_host}:{ssh_port}\n")
                    except Exception as _e:
                        self._log_queue.put(f"[!] SSH connection failed: {_e}\n")
                        return

                def _quota_cb(today, max_day, ko_today, max_ko_day):
                    parts = []
                    color = "#228b22"   # verde di default

                    if today is not None and max_day:
                        rem = max_day - today
                        pct = rem / max_day
                        parts.append(f"Scrape: {today}/{max_day}  ({rem} left)")
                        if pct <= 0.05:
                            color = "#cc0000"
                        elif pct <= 0.2:
                            color = "#cc7700"

                    if ko_today is not None and max_ko_day:
                        rem_ko = max_ko_day - ko_today
                        pct_ko = rem_ko / max_ko_day
                        parts.append(f"KO: {ko_today}/{max_ko_day}  ({rem_ko} left)")
                        # KO quota più critica: sovrascrive colore se più grave
                        if pct_ko <= 0.05:
                            color = "#cc0000"
                        elif pct_ko <= 0.2 and color == "#228b22":
                            color = "#cc7700"

                    text = "Daily quota — " + "   |   ".join(parts) if parts else "Daily quota: —"
                    self.after(0, lambda t=text, c=color:
                               self.lbl_quota.config(text=t, foreground=c))

                client = scraper.ScreenScraperClient(
                    user=user,
                    password=password,
                    devid=devid,
                    devpassword=devpass,
                )
                client.on_quota_update = _quota_cb
                s = scraper.Scraper(
                    games_dir=Path(games_dir) if not sftp_ctx else Path("/"),
                    client=client,
                    do_boxart=self.var_boxart.get(),
                    do_videos=self.var_videos.get(),
                    do_gamelist=self.var_gamelist.get(),
                    do_bezels=self.var_bezels.get(),
                    do_manuals=self.var_manuals.get(),
                    do_marquees=self.var_marquees.get(),
                    do_3dboxes=self.var_3dboxes.get(),
                    do_screenshots=self.var_screenshots.get(),
                    overwrite=self.var_overwrite.get(),
                    system_filter=opt_system,
                    folder_overrides=folder_overrides,
                    ext_override=ext_override,
                    stop_event=self._stop_event,
                    verbose=self.var_verbose.get(),
                    sftp_context=sftp_ctx,
                    sftp_remote_base=games_dir if sftp_ctx else None,
                    do_notfound_cache=self.var_notfound_cache.get(),
                )
                s.run()
                self._log_queue.put("\n✔ All done.\n")
            except Exception as e:
                self._log_queue.put(f"\n[ERROR] {e}\n")
            finally:
                if sftp_ctx:
                    try:
                        sftp_ctx.close()
                    except Exception:
                        pass
                sys.stdout = old_out
                sys.stderr = old_err
                self._log_queue.put(None)   # sentinel → worker finished

        self._worker = threading.Thread(target=worker, daemon=True)
        self._worker.start()

    def _stop(self):
        if self._worker and self._worker.is_alive():
            self._stop_event.set()
            self.lbl_status.config(text="Stopping after current ROM…")

    def _done(self):
        self.progress.stop()
        self.btn_start.config(state="normal")
        self.btn_stop.config(state="disabled")
        self.lbl_status.config(text="Done.")

    # ----------------------------------------------------------------- log --

    def _log_clear(self):
        self.log_text.config(state="normal")
        self.log_text.delete("1.0", "end")
        self.log_text.config(state="disabled")

    def _log_append(self, text):
        self.log_text.config(state="normal")
        self.log_text.insert("end", text)
        self.log_text.see("end")
        self.log_text.config(state="disabled")

    def _poll_log(self):
        """Called every 100ms from the main thread to drain the log queue."""
        try:
            while True:
                item = self._log_queue.get_nowait()
                if item is None:       # sentinel: worker finished
                    self._done()
                else:
                    self._log_append(item)
        except queue.Empty:
            pass
        self.after(100, self._poll_log)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    app = ScraperGUI()
    app.mainloop()
