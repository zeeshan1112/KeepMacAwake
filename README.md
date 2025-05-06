# StayActive

StayActive is a lightweight app that simulates small, undetectable user activity to prevent your computer from going idle or triggering sleep mode. It's like a subtle mouse jiggler — but smarter, and without physically moving your cursor.

## ✨ Features

- Keeps your computer "active" in the background
- No visible mouse movement
- Works on macOS and Windows
- Simple to use – just launch and stay active!

## 🚀 Installation

### 🖥 macOS

1. Download the latest `.dmg` file from [Releases](https://github.com/YOUR_USERNAME/StayActive/releases).
2. Open the `.dmg` and drag **StayActive.app** to your Applications folder.
3. Launch the app. Grant accessibility permissions if prompted.

### 🪟 Windows

1. Download the `.exe` installer from [Releases](https://github.com/YOUR_USERNAME/StayActive/releases).
2. Run the installer and follow the steps.
3. Launch StayActive from the Start Menu.

> ⚠️ macOS: You may need to right-click > Open the first time to bypass Gatekeeper.

## 🧪 Development

To build the app yourself:

```bash
git clone https://github.com/YOUR_USERNAME/StayActive.git
cd StayActive
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python setup.py py2app   # For macOS builds
