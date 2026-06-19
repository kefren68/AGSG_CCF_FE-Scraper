# ScreenScraper.fr — ROM file extensions per system
# Generated from ScreenScraper API (systemesListe.php)
# Format: system_id | primary_name | extensions | known_aliases
#
# Total systems with known extensions: 231

# ---------------------------------------------------------------------------
# SYSTEM_EXTENSIONS: system_id (int) -> frozenset of lowercase extensions
# (without leading dot — add '.' when comparing with Path.suffix)
# ---------------------------------------------------------------------------
SYSTEM_EXTENSIONS = {
       1: frozenset(["bin", "gen", "md", "sg", "smd", "zip"]),  # Megadrive
       2: frozenset(["bin", "sms", "zip"]),  # Master System
       3: frozenset(["bin", "fds", "fig", "nes", "unf", "zip"]),  # NES
       4: frozenset(["fig", "mgd", "sfc", "smc", "swc", "zip"]),  # Super Nintendo
       6: frozenset(["chd", "zip"]),  # Capcom Play System
       7: frozenset(["chd", "zip"]),  # Capcom Play System 2
       8: frozenset(["ccd", "chd", "img", "sub", "zip"]),  # Capcom Play System 3
       9: frozenset(["bin", "gb", "zip"]),  # Game Boy
      10: frozenset(["bin", "gb", "gbc", "zip"]),  # Game Boy Color
      11: frozenset(["bin", "vb", "vboy", "zip"]),  # Virtual Boy
      12: frozenset(["bin", "gba", "zip"]),  # Game Boy Advance
      13: frozenset(["gcz", "iso", "zip"]),  # Gamecube
      14: frozenset(["n64", "v64", "z64", "zip"]),  # Nintendo 64
      15: frozenset(["bin", "nds", "zip"]),  # Nintendo DS
      16: frozenset(["ciso", "iso", "wad", "wbfs", "zip"]),  # Wii
      17: frozenset(["3ds", "zip"]),  # Nintendo 3DS
      18: frozenset(["ciso", "iso", "wbfs", "zip"]),  # Wii U
      19: frozenset(["32x", "bin", "ccd", "cue", "img", "iso", "md", "smd", "sub", "wav", "zip"]),  # Megadrive 32X
      20: frozenset(["bin", "ccd", "chd", "cue", "img", "iso", "sub", "wav", "zip"]),  # Mega-CD
      21: frozenset(["bin", "gg", "sms", "zip"]),  # Game Gear
      22: frozenset(["bin", "chd", "cue", "iso", "m3u", "mdf", "zip"]),  # Saturn
      23: frozenset(["bin", "cdi", "chd", "elf", "gdi", "img", "m3u", "nrg", "raw", "xpm", "zip"]),  # Dreamcast
      25: frozenset(["bin", "ngc", "ngp", "zip"]),  # Neo-Geo Pocket
      26: frozenset(["a26", "bin", "rom", "zip"]),  # Atari 2600
      27: frozenset(["abs", "bin", "cof", "j64", "jag", "rom", "zip"]),  # Jaguar
      28: frozenset(["bin", "lnx", "zip"]),  # Lynx
      29: frozenset(["bin", "chd", "cue", "iso", "wav", "zip"]),  # 3DO
      30: frozenset(["id", "zip"]),  # N-Gage
      31: frozenset(["pce", "sgx", "zip"]),  # PC Engine
      32: frozenset(["iso", "zip"]),  # Xbox
      33: frozenset(["iso", "zip"]),  # Xbox 360
      34: frozenset(["iso", "zip"]),  # Xbox One
      36: frozenset(["csw", "dsk", "tap", "uef", "wav", "zip"]),  # Atom
      37: frozenset(["adf", "adl", "bin", "csw", "dsd", "m3u", "ssd", "uef", "zip"]),  # BBC Micro
      40: frozenset(["a52", "bin", "rom", "zip"]),  # Atari 5200
      41: frozenset(["a78", "bin", "rom", "zip"]),  # Atari 7800
      42: frozenset(["ctr", "dim", "img", "ipf", "msa", "raw", "rom", "st", "stx","zip"]),  # Atari ST
      43: frozenset(["a52", "asm", "atr", "atr.gz", "atx", "bas", "bin", "car", "cas", "com", "dcm", "rom", "xex", "xfd", "xfd.gz", "zip"]),  # Atari 8bit
      44: frozenset(["bin", "prg", "wav", "zip"]),  # Astrocade
      45: frozenset(["bin", "ws", "wsc", "zip"]),  # WonderSwan
      46: frozenset(["bin", "ws", "wsc", "zip"]),  # WonderSwan Color
      47: frozenset(["chd", "zip"]),  # Cave
      48: frozenset(["bin", "col", "rom","zip"]),  # Colecovision
      49: frozenset(["daphne(m2v|ogg)", "zip"]),  # Daphne
      50: frozenset(["pce", "sgx", "zip"]),  # CoreGrafX
      52: frozenset(["mgw", "zip", "zip"]),  # Game & Watch
      53: frozenset(["chd", "zip"]),  # Atomiswave
      54: frozenset(["chd", "zip"]),  # Model 2
      55: frozenset(["chd", "zip"]),  # Model 3
      56: frozenset(["bin", "chd", "gdi", "raw", "zip"]),  # Naomi
      57: frozenset(["bin", "cbn", "ccd", "chd", "cue", "img", "iso", "m3u", "mdf", "pbp", "toc", "znx", "zip"]),  # Playstation
      58: frozenset(["chd", "cue", "gz", "img", "iso", "zip"]),  # Playstation 2
      59: frozenset(["iso", "zip"]),  # Playstation 3
      60: frozenset(["iso", "zip"]),  # Playstation 4
      61: frozenset(["bin", "cso", "cue", "img", "iso", "pbp", "zip"]),  # PSP
      62: frozenset(["iso", "vpk", "zip"]),  # PS Vita
      63: frozenset(["apk", "zip"]),  # Android
      64: frozenset(["adf", "adz", "cpio", "dms", "exe", "hdf", "hdz", "ipf", "lha", "m3u", "rom", "uae", "zip"]),  # Amiga
      65: frozenset(["bin", "cpc", "cpr", "dsk","zip"]),  # CPC
      66: frozenset(["arc", "ark", "bin", "c64", "crt", "d64", "d71", "d81", "dmp", "g64", "lnx", "nbz", "nib", "p00", "prg", "reu", "sda", "sfx", "t64", "tap", "z64", "zip"]),  # Commodore 64
      67: frozenset(["bin", "cart", "zip"]),  # Super Cassette Vision
      68: frozenset(["chd", "zip"]),  # Neo-Geo MVS
      69: frozenset(["chd", "zip"]),  # Sega ST-V
      70: frozenset(["bin", "ccd", "cue", "img", "iso", "zip"]),  # Neo-Geo CD
      72: frozenset(["bin", "ccd", "chd", "cue", "img", "sub", "zip"]),  # PC-FX
      73: frozenset(["crt", "d64", "d81", "prg", "t64", "tap", "zip"]),  # Vic-20
      74: frozenset(["bin", "zip"]),  # PV-1000
      75: frozenset(["chd", "zip"]),  # Mame
      76: frozenset(["csw", "dsk", "fdi", "img", "ipf", "mgt", "rom", "rzx", "scl", "slt", "sna", "sp", "szx", "tap", "trd", "tzx", "udi", "z80", "zip"]),  # ZX Spectrum
      77: frozenset(["c", "p", "tzx", "zip"]),  # ZX81
      78: frozenset(["bin", "zip"]),  # Adventure Vision
      79: frozenset(["2hd", "7z", "88d", "cmd", "d88", "dim", "dup", "hdf", "hdm", "img", "m3u", "xdf", "zip"]),  # Sharp X68000
      80: frozenset(["bin", "zip"]),  # Channel F
      81: frozenset(["singe", "zip"]),  # Action Max
      82: frozenset(["bin", "ngc", "ngp", "zip"]),  # Neo-Geo Pocket Color
      83: frozenset(["bin", "zip"]),  # Aamber Pegasus
      84: frozenset(["adf", "cue", "iso", "jfd", "zip"]),  # Archimedes
      85: frozenset(["bin", "sdd", "uef", "zip"]),  # Electron
      86: frozenset(["do", "dsk", "nib", "po", "zip"]),  # Apple II
      87: frozenset(["bin", "cpc", "cpr", "dsk", "zip"]),  # GX4000
      88: frozenset(["ldf", "tap", "zip"]),  # Camputers Lynx
      89: frozenset(["bas", "com", "ddp", "dsk", "img", "lbr", "zip"]),  # Adam
      90: frozenset(["bin", "zip"]),  # Mega Duck
      91: frozenset(["asc", "bas", "cas", "ccc", "dmk", "dsk", "jvc", "os9", "rom", "sna", "vdk", "wav", "zip"]),  # Dragon 32/64
      92: frozenset(["cas", "zip"]),  # EG2000 Colour Genie
      93: frozenset(["bas", "bin", "bkd", "cod", "doc", "exe", "img", "mus", "pig", "zip"]),  # BK
      94: frozenset(["bin", "zip"]),  # Arcadia 2001
      95: frozenset(["bin", "zip"]),  # Game Pocket Computer
      96: frozenset(["bas", "bin", "fd", "k7", "rom", "td0", "wav", "zip"]),  # EXL 100
      97: frozenset(["d77", "t77", "zip"]),  # FM-7
      98: frozenset(["bin", "zip"]),  # Loopy
      99: frozenset(["crt", "d64", "g64", "lnx", "prg", "tap", "z64", "zip"]),  # Plus/4
     100: frozenset(["bin", "zip"]),  # Super A'can
     101: frozenset(["fpk", "smc", "zip"]),  # GP32
     102: frozenset(["bin", "gam", "vec", "zip"]),  # Vectrex
     103: frozenset(["bin", "zip"]),  # Game Master
     104: frozenset(["bin", "zip"]),  # Videopac G7000
     105: frozenset(["ccd", "cue", "pce", "sgx", "zip"]),  # PC Engine SuperGrafx
     106: frozenset(["bin", "fds", "nes", "zip"]),  # Family Computer Disk System
     107: frozenset(["sfc", "zip"]),  # Satellaview
     108: frozenset(["sfc", "smc", "st", "zip"]),  # Sufami Turbo
     109: frozenset(["bin", "sg", "zip"]),  # SG-1000
     111: frozenset(["adf", "adz", "cpio", "dms", "exe", "hdf", "hdz", "ipf", "lha", "m3u", "rom", "uae", "zip"]),  # Amiga (AGA)
     112: frozenset(["chd", "zip"]),  # Type X
     113: frozenset(["cas", "col", "dsk", "mx1", "rom", "zip"]),  # MSX
     114: frozenset(["ccd", "chd", "cue", "iso", "pce", "sgx","img", "zip"]),  # PC Engine CD-Rom
     115: frozenset(["bin", "int", "rom", "zip"]),  # Intellivision
     116: frozenset(["cas", "dsk", "mx2", "rom", "zip"]),  # MSX2
     117: frozenset(["cas", "dsk", "mx2", "rom", "zip"]),  # MSX2+
     118: frozenset(["col", "dsk", "mx1", "mx2", "rom", "zip"]),  # MSX Turbo R
     120: frozenset(["bin", "zip"]),  # V.Smile
     121: frozenset(["bin", "zip"]),  # Game.com
     122: frozenset(["ndd", "zip"]),  # Nintendo 64DD
     123: frozenset(["residualvm(residualvm)", "scummvm(scummvm)", "svm", "zip"]),  # ScummVM
     124: frozenset(["rkm", "zip"]),  # Mikrosha
     125: frozenset(["wav", "zip"]),  # Pecom 64
     126: frozenset(["a22", "ace", "asm", "dsk", "tap", "wav", "zip"]),  # Jupiter Ace
     128: frozenset(["gb", "gbc", "zip"]),  # Super Game Boy 2
     129: frozenset(["bin", "ccd", "cue", "img", "iso", "wav", "zip"]),  # Amiga CDTV
     130: frozenset(["bin", "ccd", "cdt", "cue", "img", "iso", "nrg", "sub", "zip"]),  # Amiga CD32
     131: frozenset(["bas", "bin", "dsk", "tap", "zip"]),  # Oric 1 / Atmos
     133: frozenset(["bin", "cue", "iso", "nrg", "wav","chd", "zip"]),  # CD-i
     134: frozenset(["cue", "iso", "wav", "zip"]),  # Amiga CD
     #135: frozenset(["dos(exe|com|iso|bin|mdf|ima|img|gog|dsk|z5|z8|bas|dat)", "game", "pc(exe|com|iso|bin|mdf|ima|img|gog|dsk|z5|z8|bas|dat)", "wad", "zip"]),  # PC Dos
     135: frozenset(["zip","pak"]),  # PC Dos
     136: frozenset(["dos(exe|dll|com|iso|bin|mdf|img)", "pc(exe|dll|com|iso|bin|mdf|img)", "zip"]),  # PC Win3.xx
     139: frozenset(["bin", "ccd", "cdt", "cue", "img", "iso", "nrg", "sub", "zip"]),  # Amiga CD32 (hack)
     141: frozenset(["fd", "k7", "m5", "m7", "qd", "sap", "wav", "zip"]),  # Thomson MO/TO
     142: frozenset(["chd", "zip"]),  # Neo-Geo
     144: frozenset(["asc", "bas", "cas", "ccc", "dmk", "dsk", "jvc", "os9", "rom", "sna", "vdk", "wav", "zip"]),  # TRS-80 Color Computer
     146: frozenset(["img", "rom", "zip"]),  # Mac OS
     147: frozenset(["chd", "zip"]),  # Sega Classics
     148: frozenset(["chd", "zip"]),  # Irem Classics
     149: frozenset(["chd", "zip"]),  # Seta
     150: frozenset(["chd", "zip"]),  # Midway Classics
     151: frozenset(["chd", "zip"]),  # Capcom Classics
     152: frozenset(["chd", "zip"]),  # Eighting / Raizing
     153: frozenset(["chd", "zip"]),  # Tecmo
     154: frozenset(["chd", "zip"]),  # SNK Classics
     155: frozenset(["chd", "zip"]),  # Namco Classics
     156: frozenset(["chd", "zip"]),  # Namco System 22
     157: frozenset(["chd", "zip"]),  # Taito Classics
     158: frozenset(["chd", "zip"]),  # Konami Classics
     159: frozenset(["chd", "zip"]),  # Jaleco
     160: frozenset(["chd", "zip"]),  # Atari Classics
     161: frozenset(["chd", "zip"]),  # Nintendo Classics
     162: frozenset(["chd", "zip"]),  # Data East Classics
     163: frozenset(["chd", "zip"]),  # NMK
     164: frozenset(["chd", "zip"]),  # Sammy Classics
     165: frozenset(["chd", "zip"]),  # Exidy
     166: frozenset(["chd", "zip"]),  # Acclaim
     167: frozenset(["chd", "zip"]),  # Psikyo
     169: frozenset(["chd", "zip"]),  # Technos
     170: frozenset(["chd", "cue", "iso", "zip"]),  # American Laser Games
     171: frozenset(["bin", "ccd", "cdi", "cue", "img", "nrg", "sub", "zip"]),  # Jaguar CD
     172: frozenset(["cso", "iso", "pbp", "zip"]),  # Playstation minis
     173: frozenset(["chd", "zip"]),  # Dynax
     174: frozenset(["chd", "zip"]),  # Kaneko
     175: frozenset(["chd", "zip"]),  # Video System Co.
     176: frozenset(["chd", "zip"]),  # IGS
     177: frozenset(["chd", "zip"]),  # Comad
     178: frozenset(["chd", "zip"]),  # Amcoe
     179: frozenset(["chd", "zip"]),  # Century Electronics
     180: frozenset(["chd", "zip"]),  # Nichibutsu
     181: frozenset(["chd", "zip"]),  # Visco
     182: frozenset(["chd", "zip"]),  # Alpha Denshi Co.
     183: frozenset(["chd", "zip"]),  # Coleco
     184: frozenset(["chd", "zip"]),  # PlayChoice
     185: frozenset(["chd", "zip"]),  # Atlus
     186: frozenset(["chd", "zip"]),  # Banpresto
     187: frozenset(["chd", "zip"]),  # SemiCom
     188: frozenset(["chd", "zip"]),  # Universal
     189: frozenset(["chd", "zip"]),  # Mitchell
     190: frozenset(["chd", "zip"]),  # Seibu Kaihatsu
     191: frozenset(["chd", "zip"]),  # Toaplan
     192: frozenset(["chd", "zip"]),  # Cinematronics
     193: frozenset(["chd", "zip"]),  # Incredible Technologies
     194: frozenset(["chd", "zip"]),  # Gaelco
     195: frozenset(["chd", "zip"]),  # Mega-Tech
     196: frozenset(["chd", "zip"]),  # Mega-Play
     198: frozenset(["vpt", "vpx", "zip"]),  # Visual Pinball
     199: frozenset(["ftp", "zip"]),  # Future Pinball
     200: frozenset(["chd", "zip"]),  # the Pinball Arcade
     202: frozenset(["fig", "mgd", "sfc", "smc", "swc", "zip"]),  # Snes - Super Mario World Hacks
     203: frozenset(["bin", "gen", "md", "sg", "smd", "zip"]),  # Megadrive - Sonic The Hedgehog 2 Hacks
     205: frozenset(["bin", "c", "ctg", "dsk", "g","zip"]),  # TI-99/4A
     206: frozenset(["lua", "lutro", "zip"]),  # Lutro
     207: frozenset(["bin", "sv", "zip"]),  # Watara Supervision
     208: frozenset(["2hd", "88d", "98d", "cmd", "d88", "d98", "dup", "fdd", "fdi", "hdd", "hdi", "hdm", "hdn", "nhd", "tfd", "thd", "xdf", "zip"]),  # NEC PC-9801
     209: frozenset(["chd", "zip"]),  # Gottlieb
     210: frozenset(["sfc", "zip"]),  # Super Nintendo MSU-1
     211: frozenset(["min", "zip"]),  # Pokémon mini
     213: frozenset(["dsk", "sad", "zip"]),  # MGT SAM Coupé
     214: frozenset(["pak", "zip"]),  # OpenBOR
     215: frozenset(["z1", "z2", "z3", "z4", "z5", "z6", "z7", "z8", "zip"]),  # Z-Machine
     216: frozenset(["uze", "zip"]),  # Uzebox
     217: frozenset(["2mg", "do", "dsk", "gsplus", "hdv", "nib", "po", "zip"]),  # Apple IIGS
     218: frozenset(["bin", "cas", "dsk", "zip"]),  # Spectravideo
     219: frozenset(["img", "pdb", "pqa", "prc", "zip"]),  # Palm OS
     220: frozenset(["2d", "2hd", "88d", "cmd", "d88", "dup", "dx1", "hdm", "tfd", "xdf", "zip"]),  # Sharp X1
     221: frozenset(["88d", "d88", "m3u", "zip"]),  # NEC PC-8801
     222: frozenset(["tic", "zip"]),  # TIC-80
     223: frozenset(["solarus", "zip"]),  # Solarus
     225: frozenset([".", "zip"]),  # Switch
     227: frozenset(["bin", "chd", "gdi", "raw", "zip"]),  # Naomi GD-ROM
     230: frozenset(["bin", "chd", "gdi", "raw", "zip"]),  # Naomi 2
     231: frozenset(["ini", "zip"]),  # EasyRPG
     234: frozenset(["p8", "png", "zip"]),  # Pico-8
     237: frozenset(["pc2", "zip"]),  # Pocket Challenge V2
     240: frozenset(["a0", "b0", "crt", "d64", "d81", "prg", "t64", "tap", "zip"]),  # PET
     241: frozenset(["bin", "rom", "zip"]),  # CreatiVision
     244: frozenset(["nx", "zip"]),  # LowRes NX
     250: frozenset(["md", "zip"]),  # Sega Pico
     253: frozenset(["bin", "cue", "zip"]),  # FM Towns
     258: frozenset(["zip", "zip"]),  # Hikaru
     261: frozenset(["k7", "zip"]),  # Philips VG 5000
     262: frozenset(["wasm", "zip"]),  # WASM-4
     263: frozenset(["hex", "zip"]),  # Arduboy
     266: frozenset(["bin", "zip"]),  # Gamate
     275: frozenset(["png", "vx", "zip"]),  # Voxatron
     278: frozenset(["nes", "zip"]),  # Nes - Super Mario Bros. Hacks
     284: frozenset(["iso", "zip"]),  # Playstation 5
     287: frozenset(["cas", "zip"]),  # P2000T
     290: frozenset(["wad", "zip"]),  # PrBoom
     293: frozenset(["b", "zip"]),  # Tamagotchi
     296: frozenset([".", "zip"]),  # Switch 2
     299: frozenset(["chd", "zip"]),  # Taito G-Net
     300: frozenset(["bin", "cart", "zip"]),  # Cassette Vision
     301: frozenset(["md", "zip"]),  # MSU-MD
     302: frozenset(["jar", "zip"]),  # J2ME
     305: frozenset(["myv", "zip"]),  # My Vision
     308: frozenset(["bin", "zip"]),  # V.Smile Pro
}


# ---------------------------------------------------------------------------
# Human-readable reference
# ID   | Primary Name                       | Extensions
# ---------------------------------------------------------------------------
#    1  Megadrive                             .bin, .gen, .md, .sg, .smd
#    2  Master System                         .bin, .sms
#    3  NES                                   .bin, .fds, .fig, .nes, .unf
#    4  Super Nintendo                        .fig, .mgd, .sfc, .smc, .swc
#    6  Capcom Play System                    .chd
#    7  Capcom Play System 2                  .chd
#    8  Capcom Play System 3                  .ccd, .chd, .img, .sub
#    9  Game Boy                              .bin, .gb
#   10  Game Boy Color                        .bin, .gb, .gbc
#   11  Virtual Boy                           .bin, .vb, .vboy
#   12  Game Boy Advance                      .bin, .gba
#   13  Gamecube                              .gcz, .iso
#   14  Nintendo 64                           .n64, .v64, .z64
#   15  Nintendo DS                           .bin, .nds
#   16  Wii                                   .ciso, .iso, .wad, .wbfs
#   17  Nintendo 3DS                          .3ds
#   18  Wii U                                 .ciso, .iso, .wbfs
#   19  Megadrive 32X                         .32x, .bin, .ccd, .cue, .img, .iso, .md, .smd, .sub, .wav
#   20  Mega-CD                               .bin, .ccd, .chd, .cue, .img, .iso, .sub, .wav
#   21  Game Gear                             .bin, .gg, .sms
#   22  Saturn                                .bin, .chd, .cue, .iso, .m3u, .mdf
#   23  Dreamcast                             .bin, .cdi, .chd, .elf, .gdi, .img, .m3u, .nrg, .raw, .xpm
#   25  Neo-Geo Pocket                        .bin, .ngc, .ngp
#   26  Atari 2600                            .a26, .bin, .rom
#   27  Jaguar                                .abs, .bin, .cof, .j64, .jag, .rom
#   28  Lynx                                  .bin, .lnx
#   29  3DO                                   .bin, .chd, .cue, .iso, .wav
#   30  N-Gage                                .id
#   31  PC Engine                             .pce, .sgx
#   32  Xbox                                  .iso
#   33  Xbox 360                              .iso
#   34  Xbox One                              .iso
#   36  Atom                                  .csw, .dsk, .tap, .uef, .wav
#   37  BBC Micro                             .adf, .adl, .bin, .csw, .dsd, .m3u, .ssd, .uef, .zip
#   40  Atari 5200                            .a52, .bin, .rom
#   41  Atari 7800                            .a78, .bin, .rom
#   42  Atari ST                              .ctr, .dim, .img, .ipf, .msa, .raw, .rom, .st, .stx
#   43  Atari 8bit                            .a52, .asm, .atr, .atr.gz, .atx, .bas, .bin, .car, .cas, .com, .dcm, .rom, .xex, .xfd, .xfd.gz, .zip
#   44  Astrocade                             .bin, .prg, .wav
#   45  WonderSwan                            .bin, .ws, .wsc
#   46  WonderSwan Color                      .bin, .ws, .wsc
#   47  Cave                                  .chd
#   48  Colecovision                          .bin, .col, .rom
#   49  Daphne                                .daphne(m2v|ogg)
#   50  CoreGrafX                             .pce, .sgx
#   52  Game & Watch                          .mgw
#   53  Atomiswave                            .chd
#   54  Model 2                               .chd
#   55  Model 3                               .chd
#   56  Naomi                                 .bin, .chd, .gdi, .raw
#   57  Playstation                           .bin, .cbn, .ccd, .chd, .cue, .img, .iso, .m3u, .mdf, .pbp, .toc, .znx
#   58  Playstation 2                         .chd, .cue, .gz, .img, .iso
#   59  Playstation 3                         .iso
#   60  Playstation 4                         .iso
#   61  PSP                                   .bin, .cso, .cue, .img, .iso, .pbp
#   62  PS Vita                               .iso, .vpk
#   63  Android                               .apk
#   64  Amiga                                 .adf, .adz, .cpio, .dms, .exe, .hdf, .hdz, .ipf, .lha, .m3u, .rom, .uae, .zip
#   65  CPC                                   .bin, .cpc, .cpr, .dsk
#   66  Commodore 64                          .arc, .ark, .bin, .c64, .crt, .d64, .d71, .d81, .dmp, .g64, .lnx, .nbz, .nib, .p00, .prg, .reu, .sda, .sfx, .t64, .tap, .z64
#   67  Super Cassette Vision                 .bin, .cart
#   68  Neo-Geo MVS                           .chd
#   69  Sega ST-V                             .chd
#   70  Neo-Geo CD                            .bin, .ccd, .cue, .img, .iso
#   72  PC-FX                                 .bin, .ccd, .chd, .cue, .img, .sub
#   73  Vic-20                                .crt, .d64, .d81, .prg, .t64, .tap
#   74  PV-1000                               .bin
#   75  Mame                                  .chd
#   76  ZX Spectrum                           .csw, .dsk, .fdi, .img, .ipf, .mgt, .rom, .rzx, .scl, .slt, .sna, .sp, .szx, .tap, .trd, .tzx, .udi, .z80
#   77  ZX81                                  .c, .p, .tzx
#   78  Adventure Vision                      .bin
#   79  Sharp X68000                          .2hd, .7z, .88d, .cmd, .d88, .dim, .dup, .hdf, .hdm, .img, .m3u, .xdf, .zip
#   80  Channel F                             .bin
#   81  Action Max                            .singe
#   82  Neo-Geo Pocket Color                  .bin, .ngc, .ngp
#   83  Aamber Pegasus                        .bin
#   84  Archimedes                            .adf, .cue, .iso, .jfd
#   85  Electron                              .bin, .sdd, .uef
#   86  Apple II                              .do, .dsk, .nib, .po
#   87  GX4000                                .bin, .cpc, .cpr, .dsk
#   88  Camputers Lynx                        .ldf, .tap
#   89  Adam                                  .bas, .com, .ddp, .dsk, .img, .lbr
#   90  Mega Duck                             .bin
#   91  Dragon 32/64                          .asc, .bas, .cas, .ccc, .dmk, .dsk, .jvc, .os9, .rom, .sna, .vdk, .wav
#   92  EG2000 Colour Genie                   .cas
#   93  BK                                    .bas, .bin, .bkd, .cod, .doc, .exe, .img, .mus, .pig
#   94  Arcadia 2001                          .bin
#   95  Game Pocket Computer                  .bin
#   96  EXL 100                               .bas, .bin, .fd, .k7, .rom, .td0, .wav
#   97  FM-7                                  .d77, .t77
#   98  Loopy                                 .bin
#   99  Plus/4                                .crt, .d64, .g64, .lnx, .prg, .tap, .z64
#  100  Super A'can                           .bin
#  101  GP32                                  .fpk, .smc
#  102  Vectrex                               .bin, .gam, .vec
#  103  Game Master                           .bin
#  104  Videopac G7000                        .bin
#  105  PC Engine SuperGrafx                  .ccd, .cue, .pce, .sgx
#  106  Family Computer Disk System           .bin, .fds, .nes
#  107  Satellaview                           .sfc
#  108  Sufami Turbo                          .sfc, .smc, .st
#  109  SG-1000                               .bin, .sg
#  111  Amiga (AGA)                           .adf, .adz, .cpio, .dms, .exe, .hdf, .hdz, .ipf, .lha, .m3u, .rom, .uae, .zip
#  112  Type X                                .chd
#  113  MSX                                   .cas, .col, .dsk, .mx1, .rom
#  114  PC Engine CD-Rom                      .ccd, .chd, .cue, .iso, .pce, .sgx
#  115  Intellivision                         .bin, .int, .rom
#  116  MSX2                                  .cas, .dsk, .mx2, .rom
#  117  MSX2+                                 .cas, .dsk, .mx2, .rom
#  118  MSX Turbo R                           .col, .dsk, .mx1, .mx2, .rom
#  120  V.Smile                               .bin
#  121  Game.com                              .bin
#  122  Nintendo 64DD                         .ndd
#  123  ScummVM                               .residualvm(residualvm), .scummvm(scummvm), .svm
#  124  Mikrosha                              .rkm
#  125  Pecom 64                              .wav
#  126  Jupiter Ace                           .a22, .ace, .asm, .dsk, .tap, .wav
#  128  Super Game Boy 2                      .gb, .gbc
#  129  Amiga CDTV                            .bin, .ccd, .cue, .img, .iso, .wav
#  130  Amiga CD32                            .bin, .ccd, .cdt, .cue, .img, .iso, .nrg, .sub
#  131  Oric 1 / Atmos                        .bas, .bin, .dsk, .tap
#  133  CD-i                                  .bin, .cue, .iso, .nrg, .wav
#  134  Amiga CD                              .cue, .iso, .wav
#  135  PC Dos                                .dos(exe|com|iso|bin|mdf|ima|img|gog|dsk|z5|z8|bas|dat), .game, .pc(exe|com|iso|bin|mdf|ima|img|gog|dsk|z5|z8|bas|dat), .wad, .zip
#  136  PC Win3.xx                            .dos(exe|dll|com|iso|bin|mdf|img), .pc(exe|dll|com|iso|bin|mdf|img)
#  139  Amiga CD32 (hack)                     .bin, .ccd, .cdt, .cue, .img, .iso, .nrg, .sub
#  141  Thomson MO/TO                         .fd, .k7, .m5, .m7, .qd, .sap, .wav
#  142  Neo-Geo                               .chd
#  144  TRS-80 Color Computer                 .asc, .bas, .cas, .ccc, .dmk, .dsk, .jvc, .os9, .rom, .sna, .vdk, .wav
#  146  Mac OS                                .img, .rom
#  147  Sega Classics                         .chd
#  148  Irem Classics                         .chd
#  149  Seta                                  .chd
#  150  Midway Classics                       .chd
#  151  Capcom Classics                       .chd
#  152  Eighting / Raizing                    .chd
#  153  Tecmo                                 .chd
#  154  SNK Classics                          .chd
#  155  Namco Classics                        .chd
#  156  Namco System 22                       .chd
#  157  Taito Classics                        .chd
#  158  Konami Classics                       .chd
#  159  Jaleco                                .chd
#  160  Atari Classics                        .chd
#  161  Nintendo Classics                     .chd
#  162  Data East Classics                    .chd
#  163  NMK                                   .chd
#  164  Sammy Classics                        .chd
#  165  Exidy                                 .chd
#  166  Acclaim                               .chd
#  167  Psikyo                                .chd
#  169  Technos                               .chd
#  170  American Laser Games                  .chd, .cue, .iso
#  171  Jaguar CD                             .bin, .ccd, .cdi, .cue, .img, .nrg, .sub
#  172  Playstation minis                     .cso, .iso, .pbp
#  173  Dynax                                 .chd
#  174  Kaneko                                .chd
#  175  Video System Co.                      .chd
#  176  IGS                                   .chd
#  177  Comad                                 .chd
#  178  Amcoe                                 .chd
#  179  Century Electronics                   .chd
#  180  Nichibutsu                            .chd
#  181  Visco                                 .chd
#  182  Alpha Denshi Co.                      .chd
#  183  Coleco                                .chd
#  184  PlayChoice                            .chd
#  185  Atlus                                 .chd
#  186  Banpresto                             .chd
#  187  SemiCom                               .chd
#  188  Universal                             .chd
#  189  Mitchell                              .chd
#  190  Seibu Kaihatsu                        .chd
#  191  Toaplan                               .chd
#  192  Cinematronics                         .chd
#  193  Incredible Technologies               .chd
#  194  Gaelco                                .chd
#  195  Mega-Tech                             .chd
#  196  Mega-Play                             .chd
#  198  Visual Pinball                        .vpt, .vpx
#  199  Future Pinball                        .ftp
#  200  the Pinball Arcade                    .chd
#  202  Snes - Super Mario World Hacks        .fig, .mgd, .sfc, .smc, .swc
#  203  Megadrive - Sonic The Hedgehog 2 Hacks  .bin, .gen, .md, .sg, .smd
#  205  TI-99/4A                              .bin, .c, .ctg, .dsk, .g
#  206  Lutro                                 .lua, .lutro
#  207  Watara Supervision                    .bin, .sv
#  208  NEC PC-9801                           .2hd, .88d, .98d, .cmd, .d88, .d98, .dup, .fdd, .fdi, .hdd, .hdi, .hdm, .hdn, .nhd, .tfd, .thd, .xdf
#  209  Gottlieb                              .chd
#  210  Super Nintendo MSU-1                  .sfc
#  211  Pokémon mini                          .min
#  213  MGT SAM Coupé                         .dsk, .sad
#  214  OpenBOR                               .pak
#  215  Z-Machine                             .z1, .z2, .z3, .z4, .z5, .z6, .z7, .z8
#  216  Uzebox                                .uze
#  217  Apple IIGS                            .2mg, .do, .dsk, .gsplus, .hdv, .nib, .po, .zip
#  218  Spectravideo                          .bin, .cas, .dsk, .zip
#  219  Palm OS                               .img, .pdb, .pqa, .prc
#  220  Sharp X1                              .2d, .2hd, .88d, .cmd, .d88, .dup, .dx1, .hdm, .tfd, .xdf
#  221  NEC PC-8801                           .88d, .d88, .m3u
#  222  TIC-80                                .tic
#  223  Solarus                               .solarus
#  225  Switch                                ..
#  227  Naomi GD-ROM                          .bin, .chd, .gdi, .raw
#  230  Naomi 2                               .bin, .chd, .gdi, .raw
#  231  EasyRPG                               .ini
#  234  Pico-8                                .p8, .png
#  237  Pocket Challenge V2                   .pc2
#  240  PET                                   .a0, .b0, .crt, .d64, .d81, .prg, .t64, .tap
#  241  CreatiVision                          .bin, .rom
#  244  LowRes NX                             .nx
#  250  Sega Pico                             .md
#  253  FM Towns                              .bin, .cue
#  258  Hikaru                                .zip
#  261  Philips VG 5000                       .k7
#  262  WASM-4                                .wasm
#  263  Arduboy                               .hex
#  266  Gamate                                .bin
#  275  Voxatron                              .png, .vx
#  278  Nes - Super Mario Bros. Hacks         .nes
#  284  Playstation 5                         .iso
#  287  P2000T                                .cas
#  290  PrBoom                                .wad
#  293  Tamagotchi                            .b
#  296  Switch 2                              ..
#  299  Taito G-Net                           .chd
#  300  Cassette Vision                       .bin, .cart
#  301  MSU-MD                                .md
#  302  J2ME                                  .jar
#  305  My Vision                             .myv
#  308  V.Smile Pro                           .bin


# ---------------------------------------------------------------------------
# SYSTEM_NAMES: system_id (int) -> primary display name
# Includes all systems known to ScreenScraper (with or without extensions)
# ---------------------------------------------------------------------------
SYSTEM_NAMES = {
       1: "Megadrive",
       2: "Master System",
       3: "NES",
       4: "Super Nintendo",
       6: "Capcom Play System",
       7: "Capcom Play System 2",
       8: "Capcom Play System 3",
       9: "Game Boy",
      10: "Game Boy Color",
      11: "Virtual Boy",
      12: "Game Boy Advance",
      13: "Gamecube",
      14: "Nintendo 64",
      15: "Nintendo DS",
      16: "Wii",
      17: "Nintendo 3DS",
      18: "Wii U",
      19: "Megadrive 32X",
      20: "Mega-CD",
      21: "Game Gear",
      22: "Saturn",
      23: "Dreamcast",
      25: "Neo-Geo Pocket",
      26: "Atari 2600",
      27: "Jaguar",
      28: "Lynx",
      29: "3DO",
      30: "N-Gage",
      31: "PC Engine",
      32: "Xbox",
      33: "Xbox 360",
      34: "Xbox One",
      36: "Atom",
      37: "BBC Micro",
      39: "Atari 2600 Supercharger",
      40: "Atari 5200",
      41: "Atari 7800",
      42: "Atari ST",
      43: "Atari 8bit",
      44: "Astrocade",
      45: "WonderSwan",
      46: "WonderSwan Color",
      47: "Cave",
      48: "Colecovision",
      49: "Daphne",
      50: "CoreGrafX",
      52: "Game & Watch",
      53: "Atomiswave",
      54: "Model 2",
      55: "Model 3",
      56: "Naomi",
      57: "Playstation",
      58: "Playstation 2",
      59: "Playstation 3",
      60: "Playstation 4",
      61: "PSP",
      62: "PS Vita",
      63: "Android",
      64: "Amiga",
      65: "CPC",
      66: "Commodore 64",
      67: "Super Cassette Vision",
      68: "Neo-Geo MVS",
      69: "Sega ST-V",
      70: "Neo-Geo CD",
      72: "PC-FX",
      73: "Vic-20",
      74: "PV-1000",
      75: "Mame",
      76: "ZX Spectrum",
      77: "ZX81",
      78: "Adventure Vision",
      79: "Sharp X68000",
      80: "Channel F",
      81: "Action Max",
      82: "Neo-Geo Pocket Color",
      83: "Aamber Pegasus",
      84: "Archimedes",
      85: "Electron",
      86: "Apple II",
      87: "GX4000",
      88: "Camputers Lynx",
      89: "Adam",
      90: "Mega Duck",
      91: "Dragon 32/64",
      92: "EG2000 Colour Genie",
      93: "BK",
      94: "Arcadia 2001",
      95: "Game Pocket Computer",
      96: "EXL 100",
      97: "FM-7",
      98: "Loopy",
      99: "Plus/4",
     100: "Super A'can",
     101: "GP32",
     102: "Vectrex",
     103: "Game Master",
     104: "Videopac G7000",
     105: "PC Engine SuperGrafx",
     106: "Family Computer Disk System",
     107: "Satellaview",
     108: "Sufami Turbo",
     109: "SG-1000",
     110: "Nintendo Power",
     111: "Amiga (AGA)",
     112: "Type X",
     113: "MSX",
     114: "PC Engine CD-Rom",
     115: "Intellivision",
     116: "MSX2",
     117: "MSX2+",
     118: "MSX Turbo R",
     119: "GBA e-Reader",
     120: "V.Smile",
     121: "Game.com",
     122: "Nintendo 64DD",
     123: "ScummVM",
     124: "Mikrosha",
     125: "Pecom 64",
     126: "Jupiter Ace",
     127: "Super Game Boy",
     128: "Super Game Boy 2",
     129: "Amiga CDTV",
     130: "Amiga CD32",
     131: "Oric 1 / Atmos",
     133: "CD-i",
     134: "Amiga CD",
     135: "PC Dos",
     136: "PC Win3.xx",
     137: "PC Win9X",
     138: "PC Windows",
     139: "Amiga CD32 (hack)",
     141: "Thomson MO/TO",
     142: "Neo-Geo",
     143: "Pinball FX2",
     144: "TRS-80 Color Computer",
     145: "Linux",
     146: "Mac OS",
     147: "Sega Classics",
     148: "Irem Classics",
     149: "Seta",
     150: "Midway Classics",
     151: "Capcom Classics",
     152: "Eighting / Raizing",
     153: "Tecmo",
     154: "SNK Classics",
     155: "Namco Classics",
     156: "Namco System 22",
     157: "Taito Classics",
     158: "Konami Classics",
     159: "Jaleco",
     160: "Atari Classics",
     161: "Nintendo Classics",
     162: "Data East Classics",
     163: "NMK",
     164: "Sammy Classics",
     165: "Exidy",
     166: "Acclaim",
     167: "Psikyo",
     168: "non Jeu",
     169: "Technos",
     170: "American Laser Games",
     171: "Jaguar CD",
     172: "Playstation minis",
     173: "Dynax",
     174: "Kaneko",
     175: "Video System Co.",
     176: "IGS",
     177: "Comad",
     178: "Amcoe",
     179: "Century Electronics",
     180: "Nichibutsu",
     181: "Visco",
     182: "Alpha Denshi Co.",
     183: "Coleco",
     184: "PlayChoice",
     185: "Atlus",
     186: "Banpresto",
     187: "SemiCom",
     188: "Universal",
     189: "Mitchell",
     190: "Seibu Kaihatsu",
     191: "Toaplan",
     192: "Cinematronics",
     193: "Incredible Technologies",
     194: "Gaelco",
     195: "Mega-Tech",
     196: "Mega-Play",
     197: "Flipper",
     198: "Visual Pinball",
     199: "Future Pinball",
     200: "the Pinball Arcade",
     201: "Pinball FX3",
     202: "Snes - Super Mario World Hacks",
     203: "Megadrive - Sonic The Hedgehog 2 Hacks",
     205: "TI-99/4A",
     206: "Lutro",
     207: "Watara Supervision",
     208: "NEC PC-9801",
     209: "Gottlieb",
     210: "Super Nintendo MSU-1",
     211: "Pokémon mini",
     213: "MGT SAM Coupé",
     214: "OpenBOR",
     215: "Z-Machine",
     216: "Uzebox",
     217: "Apple IIGS",
     218: "Spectravideo",
     219: "Palm OS",
     220: "Sharp X1",
     221: "NEC PC-8801",
     222: "TIC-80",
     223: "Solarus",
     225: "Switch",
     227: "Naomi GD-ROM",
     230: "Naomi 2",
     231: "EasyRPG",
     234: "Pico-8",
     237: "Pocket Challenge V2",
     240: "PET",
     241: "CreatiVision",
     244: "LowRes NX",
     250: "Sega Pico",
     253: "FM Towns",
     258: "Hikaru",
     261: "Philips VG 5000",
     262: "WASM-4",
     263: "Arduboy",
     266: "Gamate",
     269: "TeknoParrot",
     272: "Vircon32",
     275: "Voxatron",
     278: "Nes - Super Mario Bros. Hacks",
     281: "VC 4000",
     284: "Playstation 5",
     287: "P2000T",
     290: "PrBoom",
     293: "Tamagotchi",
     296: "Switch 2",
     299: "Taito G-Net",
     300: "Cassette Vision",
     301: "MSU-MD",
     302: "J2ME",
     305: "My Vision",
     308: "V.Smile Pro",
}
