import logging
import rumps
import threading
import time
import os
import webbrowser

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Flag to indicate if the Quartz framework is available for mouse events
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
        if quartz_available:
            try:
                # Create a mouse move event
                event = CGEventCreateMouseEvent(None, kCGEventMouseMoved, (100, 100), 0)
                # Post the event to the system event queue
                CGEventPost(kCGHIDEventTap, event)
                logging.info("Mouse moved.")
            except Exception as e:
                logging.error(f"Error moving mouse: {e}")
        time.sleep(30) # Wait for 30 seconds before moving the mouse again
        logging.info("Mouse movement thread stopped.")

class KeepMacAwake(rumps.App):
    """
    A rumps application that prevents the system from going idle by periodically moving the mouse.
    """
    def __init__(self):
        """
        Initializes the KeepMacAwake. Sets up the menu items, icon, and the initial state.
        """
        self.app_version = "2.0.2"
        self.app_copyright = "Copyright © 2025 Zeeshan Ahmad. All Rights Reserved."
        self.app_website_url = "https://keepmacawake.netlify.app/"

        icon_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'assets', 'icon.png'))
        if not os.path.exists(icon_path):
            icon_path = os.path.join(os.path.dirname(__file__), 'icon.png')
        super(KeepMacAwake, self).__init__("KeepMacAwake", icon=icon_path)
        logging.info(f"Application initialized with icon: {icon_path}")

        # Create menu items for starting and stopping the activity
        self.start_item = rumps.MenuItem("Start", callback=self.start_clicked)
        self.stop_item = rumps.MenuItem("Stop", callback=self.stop_clicked)

        self.about_item = rumps.MenuItem("About KeepMacAwake", callback=self.open_app_website)

        # Define the application menu
        self.menu = [self.about_item, None, self.start_item, self.stop_item, None]

        # Use a timer to ensure the 'Stop' item is disabled after the menu is built.
        # This addresses a potential race condition or initialization order issue.
        self.disable_timer = rumps.Timer(self._disable_stop_item, 0.1)
        self.disable_timer.start()

        self.running_thread = None
        logging.info("Menu items created and timer for disabling 'Stop' started.")

    def _disable_stop_item(self, sender):
        """
        Callback function for the timer to disable the 'Stop' menu item after a short delay.
        Args:
            sender: The rumps.Timer object.
        """
        logging.debug("Disabling stop item")
        self.stop_item.set_callback(None)
        self.disable_timer.stop()
        logging.info("'Stop' menu item disabled.")

    @rumps.notifications
    def notify_user(self, message):
        """
        Displays a rumps notification to the user.
        Args:
            message (str): The message to display in the notification.
        """
        rumps.notification("KeepMacAwake", "", message)
        logging.info(f"Notification sent: {message}")
    
    @rumps.clicked("About KeepMacAwake")
    def open_app_website(self, _):
        """
        Opens the application's dedicated website/about page in the default web browser.
        This replaces the old rumps.alert 'About' box.
        """
        try:
            webbrowser.open_new(self.app_website_url)
            logging.info(f"Opened app website: {self.app_website_url}")
        except Exception as e:
            # Fallback to an alert if the browser cannot be opened for some reason
            rumps.alert(title="Error", message=f"Could not open web page:\n{self.app_website_url}\n\nError: {e}")
            logging.error(f"Error opening app website: {e}")

    @rumps.clicked("Start")
    def start_clicked(self, _):
        """
        Callback function when the 'Start' menu item is clicked.
        Starts the mouse movement thread and updates the menu items.
        Args:
            _: Not used.
        """
        global running
        if not running:
            running = True
            logging.info("Starting mouse movement.")
            self.running_thread = threading.Thread(target=move_mouse, daemon=True)
            self.running_thread.start()
            self.notify_user("Started successfully.")
            self.start_item.title = "Running..."
            self.start_item.set_callback(None) # Disable the 'Start' button
            self.stop_item.set_callback(self.stop_clicked) # Enable the 'Stop' button
            logging.info("Mouse movement started and menu updated.")
        else:
            logging.warning("Attempted to start when already running.")

    @rumps.clicked("Stop")
    def stop_clicked(self, _):
        """
        Callback function when the 'Stop' menu item is clicked.
        Stops the mouse movement thread and resets the menu items.
        Args:
            _: Not used.
        """
        global running
        if running:
            running = False
            logging.info("Stopping mouse movement.")
            self.notify_user("Stopped.")

            # Update the menu items: change back to Start, disable Stop
            self.start_item.title = "Start"  # Change back to Start
            self.start_item.set_callback(self.start_clicked) # Enable Start button
            self.stop_item.set_callback(None)
            logging.info("Mouse movement stopped and menu updated.")
        else:
            logging.warning("Attempted to stop when already stopped.")

if __name__ == "__main__":
    """
    Main entry point of the application. Checks for Quartz availability and runs the rumps app.
    """
    logging.info("Application starting.")
    if not quartz_available:
        logging.warning("Quartz module not found.\nMouse movement won't work.")
        rumps.alert("Quartz module not found.\nMouse movement won't work.")
    KeepMacAwake().run()
    logging.info("Application finished.")
