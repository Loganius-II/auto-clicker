import pyautogui as pag
from time import sleep
import win32con, win32api
import subprocess
import os
import keyboard

def click(x: str | float, y: str | float) -> None:
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

def tipe(message: str, speed: float = 0.03):
    #iterate through each letter in message to display a type writer effect
    for letter in message:
        print(letter, end="", flush=True)
        sleep(speed)
    #start new line
    print()

def main() -> None:
    tipe("AUTO-GAME-CLICKER")
    tipe("author: Logan McDermott")
    tipe("Popular uses:\n1. To keep mouse active during work\n2. Banana steam game")
    tipe("3. Other clicker games")
    tipe("Enter to continue...")
    input()
    os.system('cls') if os.name == 'nt' else os.system('clear')
    tipe("Put your cursor where you want to rapid click\nPress Enter when you are ready...")
    input()
    mouse_x, mouse_y = win32api.GetCursorPos()
    tipe("Clicking...\nPress E to exit")
    while True:
        if keyboard.is_pressed('e'):
            break
        try:
            click(mouse_x, mouse_y)
            sleep(0.0001)
        except KeyboardInterrupt:
            print("Interrupt recieved, exiting...")
            break
        except Exception as e:
            print(e)
            break
if __name__ == main():
    main()