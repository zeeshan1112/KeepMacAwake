from setuptools import setup

APP = ['main.py']
DATA_FILES = ['icon.png']
OPTIONS = {
    # 'argv_emulation': True,
    'iconfile': 'icon.png',
    'packages': ['rumps', 'Quartz'],
    # 'excludes': ['jaraco'],
    'plist': {
        'CFBundleName': 'StayActive',
        'CFBundleDisplayName': 'StayActive',
        'CFBundleIdentifier': 'com.zeeshan.stayactive',
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
