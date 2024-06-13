import psutil
import time
import os

def shutdown():
    os.system("shutdown /s /t 0")


def check_ethernet_connection():
    interfaces = psutil.net_if_stats()
    if 'Ethernet' in interfaces:
        if interfaces['Ethernet'].isup:
            print("Ethernet connection is up", end="\r")
        else:
            shutdown()
            print("Ethernet connection is down")
    else:
        print("Ethernet interface not found")

if __name__ == "__main__":
    while True:
        check_ethernet_connection()
        time.sleep(1)  # Check every second
