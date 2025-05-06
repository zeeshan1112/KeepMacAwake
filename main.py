import logging
import rumps
import threading
import time
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

try:
    from Quartz.CoreGraphics import (
        CGEventCreateMouseEvent,
        CGEventPost,
        kCGEventMouseMoved,
        kCGHIDEventTap
    )
    quartz_available = True
    logging.info("Quartz framework is available.")
except ImportError:
    quartz_available = False
    logging.warning("Quartz framework not found. Mouse movement will be disabled.")

# Global flag to control the mouse movement thread
running = False

def move_mouse():
    """
    Moves the mouse cursor slightly at a fixed interval to prevent the system from going idle.
    This function runs in a separate thread.
    """
    logging.info("Mouse movement thread started.")
    while running:
        logging.debug("Moving mouse...")
        if quartz_available:
            CGEventPost(kCGHIDEventTap, CGEventCreateMouseEvent(
                None, kCGEventMouseMoved, (100, 100), 0))
        time.sleep(30)

class StayActiveApp(rumps.App):
    def __init__(self):
        logging.debug("Initializing StayActiveApp")
        icon_path = os.path.join(os.path.dirname(__file__), "icon.png")
        super(StayActiveApp, self).__init__("StayActive", icon=icon_path)

        # Create MenuItems
        self.start_item = rumps.MenuItem("Start", callback=self.start_clicked)
        self.stop_item = rumps.MenuItem("Stop", callback=self.stop_clicked)
        self.menu = [self.start_item, self.stop_item, None]

        self.disable_timer = rumps.Timer(self._disable_stop_item, 0.1)
        self.disable_timer.start()
        self.running_thread = None

    def _disable_stop_item(self, sender):
        logging.debug("Disabling stop item")
        self.stop_item.set_callback(None)
        self.disable_timer.stop()

    @rumps.notifications
    def notify_user(self, message):
        logging.debug("Notify user: %s", message)
        rumps.notification("StayActive", "", message)
    
    @rumps.clicked("Start")
    def start_clicked(self, _):
        global running
        logging.debug("Start clicked")
        if not running:
            running = True
            self.running_thread = threading.Thread(target=move_mouse, daemon=True)
            self.running_thread.start()
            self.notify_user("Started successfully.")
            self.start_item.title = "Running..."
            # Update the menu items: disable Start, enable Stop
            self.start_item.set_callback(None)
            self.stop_item.set_callback(self.stop_clicked)

    @rumps.clicked("Stop")
    def stop_clicked(self, _):
        global running
        running = False
        logging.debug("Stop clicked")
        self.notify_user("Stopped.")

        # Update the menu items: change back to Start, disable Stop
        self.start_item.title = "Start"  # Change back to Start
        self.start_item.set_callback(self.start_clicked) # Enable Start button
        self.stop_item.set_callback(None)

if __name__ == "__main__":

    if not quartz_available:
        logging.warning("Quartz module not found.\nMouse movement won't work.")
        rumps.alert("Quartz module not found.\nMouse movement won't work.")
    StayActiveApp().run()
