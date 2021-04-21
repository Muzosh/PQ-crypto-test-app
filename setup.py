import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

options = {
    "build_exe": {
        # exclude packages that are not really needed
        "excludes": [
            "tkinter",
            "unittest",
            "email",
            "http",
            "xml",
            "pydoc",
            "pdb",
        ],
        "includes": [
            "PySide2",
            "json",
            "Cryptodome"
        ],
        "include_files":[
            "Gui",
            "Managers"
        ]
    }
}

executables = [
    Executable("Gui/main.py", base=base, target_name="PQCrypto")
]

setup(
    name="PQCrypto",
    version="2022",
    description="Semestral project based around PostQuantum Cryptography",
    author="Design: Wanderson M. Pimenta | Created: Bc. Dzadíková, Bc. Janout, Bc. Lovinger, Bc. Muzikant",
    options=options,
    executables=executables
)