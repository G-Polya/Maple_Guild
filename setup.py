from cx_Freeze import setup, Executable
import cx_Freeze
import matplotlib
import sys
import numpy
import tkinter

buildOptions = dict(packages = ["idna","re","sys","os"],  # 1
	excludes = ["tkinter", "PyQt4.QtSql", "sqlite3"])

base = "Win32GUI"

if sys.platform == "win32":
    base = "Win32GUI"

exe = [Executable("Maple_UI.py",base=base)]  # 2



# 3
setup(
    name='Test Application',
    version = '0.1',
    author = "IML",
    description = "I'M IML!",
    options = dict(build_exe = buildOptions),
    executables = exe
)
