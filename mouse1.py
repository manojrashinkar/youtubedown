import pyautogui
import time
while True:
    pyautogui.moveRel(50, 100)
    time.sleep(2)
    pyautogui.moveRel(-50, -100)
    time.sleep(2)
