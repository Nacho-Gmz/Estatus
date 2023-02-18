import sys, os
from cx_Freeze import setup, Executable

files = ['ui_mainwindow.py','mainwindow.py']

exe = Executable(script='main.py',base='Win32GUI')

setup(
    name="Agenda de contactos",
    options={'build_exe':{'include_files': files}},
    version='1.0',
    description="Agenda para guardar contactos",
    author="Nacho Gomez",
    executables = [exe]
)