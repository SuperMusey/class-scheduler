import pyautogui
import time

# Prevent screen from blanking
while True:
    print("Moving....")
    pyautogui.moveRel(2, 2)  # Move the cursor slightly
    time.sleep(30)  # Repeat every 30 seconds
    pyautogui.moveRel(-2, -2)  # Move the cursor slightly
    time.sleep(30)  # Repeat every 30 seconds
