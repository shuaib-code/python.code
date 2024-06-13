import subprocess
import time

def check_internet():
    try:
        subprocess.check_call(['ping', '-c', '1', '8.8.8.8'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("Connected to the internet")
    except subprocess.CalledProcessError:
        print("No internet connection")

if __name__ == "__main__":
    while True:
        check_internet()
        time.sleep(1)  # Check every second