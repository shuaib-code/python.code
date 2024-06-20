import psutil
import time
import os

ups_time = 4  # in minutes

def shutdown():
    os.system("shutdown /s /t 0")

def eth_up():
    iface = psutil.net_if_stats().get('Ethernet')
    return iface and iface.isup

if __name__ == "__main__":
    while True:
        if eth_up():
            time.sleep(1)
        else:
            wait_secs = int((ups_time / 2) * 60)
            start = time.time()
            while time.time() - start < wait_secs:
                if eth_up():
                    break
                time.sleep(1)
            else:
                shutdown()
                break

            ups_time /= 2

            time.sleep(1)
