from setuptools import find_packages
from cx_Freeze import setup, Executable

options = {
    'build_exe': {
        'include_files': ['pages/', ('assets/fonts.css', 'assets/'), ('assets/panthers_logo.png','assets/'), ('assets/IntegralCF-Regular.otf','assets/'),('assets/IntegralCF-RegularOblique.otf','assets/'), 'songs/'],
        'includes': [
            'cx_Logging', 'idna'
        ],
    }
}

executables = [
    Executable(
        'index.py',
        targetName='WalkUpSongsApp.exe',
        icon='favicon.ico'
    )
]

setup(
    name='Walk Up Song App',
    version='0.0.1',
    description='Walk Up Song App',
    executables=executables,
    options=options,
)