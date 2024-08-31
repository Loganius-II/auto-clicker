from time import sleep
import win32con, win32api
import keyboard
import pygame

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

def clicker() -> None:
    mouse_x, mouse_y = win32api.GetCursorPos()
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

def main() -> None:
    print("Press Q to start, E to stop, and ` to exit code")
    while True:
        if keyboard.is_pressed('q'):
            clicker()

        if keyboard.is_pressed("`"):
            break
if __name__ == main():
    main()
