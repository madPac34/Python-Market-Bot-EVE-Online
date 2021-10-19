from cx_Freeze import setup, Executable

base = None    

executables = [Executable("Python_Market_Application.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "Market Updater>",
    options = options,
    version = "<1.1>",
    description = '<Auto Updates Eve Market Orders>',
    executables = executables )