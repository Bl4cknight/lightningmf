from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages=[], excludes=[], include_files=['lightningmf_pk/view.ui', 'lightningmf_pk/config.ui', 'lightningmf_pk/logo.svg'])

import sys
base = 'Win32GUI' if sys.platform == 'win32' else None

executables = [
    Executable('lightningmf', base=base)
]


setup(name='lightningmf',
      version='1.0',
      description='Python MAME frontend',
      options=dict(build_exe=buildOptions),
      executables=executables)
