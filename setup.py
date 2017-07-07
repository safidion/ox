from cx_Freeze import setup, Executable
import os
import sys

os.environ['TCL_LIBRARY'] = r'C:\Program Files\Python35-32\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Program Files\Python36-32\tcl\tk8.6'

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages=["tkinter"], excludes=[], includes=["tkinter"],
                    include_files=["C:\Program Files\Python36-32\DLLs\\tcl86t.dll",
                                   "C:\Program Files\Python36-32\dlls\\tk86t.dll"]
                    )

base = 'Win32GUI' if sys.platform == 'win32' else None

executables = [Executable('ox_main.py', base=base)]

setup(
    name='ox',
    version='0.1',
    description='The best game ox',
    options=dict(build_exe=buildOptions),
    executables=executables
)
'''
from cx_Freeze import setup, Executable  
import sys  

build_exe_options = {"packages": ["files", "tools"], "include_files": ["C:\Program Files\Python36-32\DLLs\\tcl86t.dll", "C:\Program Files\Python36-32\dlls\\tk86t.dll"]}  

base = None  
if sys.platform == "win32":  
    base = "Win32GUI"  

setup(name="Name",  
    version="1.0",  
    description="Description",  
    options={"build_exe": build_exe_options},  
    executables=[Executable("main.py", base=base)],  
    package_dir={'': ''},  
    ) 
'''
