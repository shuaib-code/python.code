import pyautogui
import time

time.sleep(7)
i = 0
for message in range(1000):
    pyautogui.typewrite(f"{i}")
    i = i+1
    pyautogui.press('enter')

