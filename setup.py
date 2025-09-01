from setuptools import setup

APP = ['src/keepmacawake/main.py']
DATA_FILES = ['assets/icon.png']
OPTIONS = {
    'iconfile': 'assets/icon.png',
    'packages': ['rumps', 'Quartz'],
    'includes': ['imp'],
    'plist': {
        'CFBundleName': 'KeepMacAwake',
        'CFBundleDisplayName': 'KeepMacAwake',
        'CFBundleIdentifier': 'com.zeeshan.keepmacawake',
        'CFBundleVersion': '0.1.0',
        'LSUIElement': True,  # hides dock icon
    }
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
