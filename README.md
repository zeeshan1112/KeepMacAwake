<p align="center">
  <img src="icon.png" alt="StayActive Icon" width="120" />
</p>

<h1 align="center">StayActiveApp</h1>

StayActiveApp is a lightweight macOS utility that simulates subtle, undetectable user activity to prevent your Mac from going idle or triggering sleep mode. It ensures your screen stays on and your apps remain active, without any visible mouse movement.

## ✨ Features

- Keeps your Mac "active" in the background
- No visible mouse cursor movement
- Runs seamlessly from your macOS menu bar
- Simple to use – just launch and stay active!

## 🚀 Installation

### 🖥 macOS

1.  **Identify your Mac's Chip:** Before downloading, determine your Mac's processor type to ensure you download the correct version:
    * Click the **Apple menu** () in the top-left corner of your screen.
    * Select **"About This Mac"**.
    * Look for the "Chip" or "Processor" entry:
        * If it says **"Apple M1," "Apple M2," "Apple M3,"** etc., you have an **Apple Silicon (ARM) Mac**.
        * If it says **"Intel"** (e.g., "Intel Core i5", "Intel Core i7"), you have an an **Intel Mac**.

2.  Download the latest `.dmg` file for your chip type from [Releases](https://github.com/zeeshan1112/StayActiveApp/releases). You will find files named like `StayActive_X.Y.Z_Intel.dmg` or `StayActive_X.Y.Z_AppleSilicon.dmg`.

3.  Open the downloaded `.dmg` file and drag **StayActive.app** to your Applications folder.

> ⚠️ **First Launch Warning (Gatekeeper):**
> The first time you launch StayActiveApp, macOS Gatekeeper might prevent it from opening because the app is downloaded from the internet and not from the Mac App Store.
>
> To bypass this:
> 1.  **Try opening directly:**
>     * **Right-click** (or Control-click) on **StayActive.app** in your Applications folder.
>     * Select **"Open"** from the context menu.
>     * A dialog box should appear with an **"Open"** button. Click it to confirm.
> 2.  **If the "Open" button is not present in the dialog:**
>     * Go to **System Settings** (or System Preferences).
>     * Click on **Privacy & Security** in the sidebar.
>     * In the "Security" section at the top, you should see a message about "StayActive" being blocked. Click the **"Open Anyway"** button next to this message. You'll likely be prompted to confirm again.
>
> You should only need to do this bypass once.

### Important Setup Steps

For StayActiveApp to function correctly and provide updates, you need to grant it specific permissions on your macOS system.

#### 1. Granting Accessibility Permission (Required for Mouse Movement)

StayActiveApp needs permission to "control your computer" to perform the slight, undetectable mouse movements that prevent your Mac from going to sleep. This is a standard macOS security measure for apps that automate input.

**If StayActiveApp doesn't seem to be working (e.g., your Mac still sleeps, or you don't see the mouse movement effect):**

1.  Go to **System Settings** (or **System Preferences** on older macOS versions).
2.  Click on **Privacy & Security** in the sidebar.
3.  Scroll down and click on **Accessibility**.
4.  You may need to click the **unlock icon** in the bottom left corner and enter your administrator password.
5.  In the list of applications, locate **"StayActive"**.
    * If "StayActive" is already in the list, make sure its checkbox is **ticked (enabled)**.
    * If "StayActive" is *not* in the list, click the **`+` (plus) button** below the list, navigate to your `/Applications` folder (or wherever you dragged `StayActive.app`), select **"StayActive.app"**, and then click **"Open"**. Once added, make sure its checkbox is **ticked**.
6.  Close System Settings.
7.  If StayActiveApp was already running, you might need to **restart the StayActiveApp** from your menu bar for the changes to take effect.

#### 2. Allowing Notifications (Optional)

StayActiveApp can send notifications to let you know when it starts and stops. If you wish to receive these notifications:

1.  Go to **System Settings** (or **System Preferences**).
2.  Click on **Notifications**.
3.  Scroll down the list of applications on the left sidebar and locate **"StayActive"**.
4.  Click on "StayActive" and adjust its notification settings to your preference (e.g., enable "Allow Notifications," choose "Banners" or "Alerts").

## 🧪 Development

To build the app yourself:

```bash
git clone [https://github.com/zeeshan1112/StayActive.git](https://github.com/zeeshan1112/StayActive.git)
cd StayActiveApp
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python setup.py py2app   # For macOS builds