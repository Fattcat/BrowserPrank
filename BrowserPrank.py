import webbrowser
import pyautogui
import time
import random
import os
import keyboard

#                ! DISCLAIMER !
#         ! This code is ONLY FOR FUN !
# ! DONT USE IT ON ANY PC WITHOUT PERMISSION !

os.system("cls")
PressIt = pyautogui.hotkey("win", "d")

KeyList = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
           "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
           "u", "v", "w", "x", "y", "z",
           ",", ".", "-", "enter", "&", ";", ":", "<", ">", "_",
           # "esc", je ODKOMENTOVANE pre to, aby sa script dal vypnut esc klavesou
           "alt", "altgr", "ctrl", "shift", "tab", "win", "+",
           "space", "backspace", "delete", "insert", "home", "end", "page up", "page down",
           "up", "down", "left", "right", "print screen", "num lock", "scroll lock", "pause",
           "f1", "f2", "f3", "f4","f5", "f6", "f7", "f8", "f9", "f10", "f11", "f12"]
while True:
    for Klavesa in KeyList:
        if keyboard.is_pressed(Klavesa):
            print(PressIt)
            print("stlačené !", Klavesa)
            webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        else:
            pass            
    if keyboard.is_pressed("esc"):
        print("Stlacene ESC!\nExitting and Leaving ...")
        exit()

    CLICKER = True

#    if CLICKER:
#        time.sleep(2)
#        pyautogui.click()
