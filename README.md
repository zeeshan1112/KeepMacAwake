<p align="center">
  <img src="icon.png" alt="StayActive Icon" width="120" />
</p>

<h1 align="center">StayActiveApp</h1>


StayActiveApp is a lightweight app that simulates small, undetectable user activity to prevent your computer from going idle or triggering sleep mode. It's like a subtle mouse jiggler — but smarter, and without physically moving your cursor.

## ✨ Features

- Keeps your computer "active" in the background
- No visible mouse movement
- Works on macOS and Windows
- Simple to use – just launch and stay active!

## 🚀 Installation

### 🖥 macOS

1. Download the latest `.dmg` file from [Releases](https://github.com/zeeshan1112/StayActiveApp/releases).
2. Open the `.dmg` and drag **StayActive.app** to your Applications folder.
3. Launch the app. Grant accessibility permissions if prompted.

> ⚠️ macOS: You may need to right-click > Open the first time to bypass Gatekeeper.

### 🪟 Windows (Coming Soon)

1. Download the `.exe` installer from [Releases](https://github.com/zeeshan1112/StayActiveApp/releases) (Not available yet).
2. Run the installer and follow the steps.
3. Launch StayActive from the Start Menu.

> ⚠️ Windows: Installation is in progress and will be released soon.

## 🧪 Development

To build the app yourself:

```bash
git clone https://github.com/zeeshan1112/StayActive.git
cd StayActiveApp
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python setup.py py2app   # For macOS builds
