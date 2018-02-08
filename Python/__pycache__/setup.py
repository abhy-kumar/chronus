from cx_Freeze import setup, Executable

base = None


executables = [Executable("rss_core.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {

        'packages': packages,
    },

}

setup(
    name = "Chronus",
    options = options,
    version = "0.1",
    description = 'Cross Platform RSS Reader',
    executables = executables
)