import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["os", "sqlite3", "requests", "bs4", "queue", "idna.idnadata"],
                     "excludes": ["tkinter"],
                     "include_files": ["img", "model", "ui", "utils"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(name="FUT19",
      version="3.0",
      description="Business FUT",
      options={"build_exe": build_exe_options},
      executables=[Executable(script="main.py",
                              base=base,
                              icon="img/fut_icon.ico",
                              targetName="FUT19.exe")])