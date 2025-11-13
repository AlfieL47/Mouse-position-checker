#Used for checking position of things on screen for making other code, mouse location output either every second or when designated button is pressed

import time
import keyboard
import pyautogui 

exit = "-" #Change to whatever button should stop code
recordbutton = "=" #change to whatever button is ideal <=====================================================


print(f"hold {exit} to stop code")
resp = input(f"Constant or each time {recordbutton} is pressed (C/E)")
resp = resp.lower()

#repeated recording
if resp == "c":
    while True:
        print(f"mouse position at {pyautogui.position()}")
        time.sleep(1)
        if keyboard.is_pressed(exit):
            quit()
    
#recording every set button press
elif resp == "e":
    while True:
        if keyboard.is_pressed(recordbutton):
            time.sleep(0.15) #stops it sending multiple times
            print(f"mouse position at {pyautogui.position()}")
        if keyboard.is_pressed(exit):
            quit()

            