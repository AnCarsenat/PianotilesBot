import mouseinfo ; import keyboard ; import pyautogui ; import time ; import win32api ; import win32con
import asyncio



#ZOOM = 75% on chrome

#GAME LINK = https://lagged.com/en/g/magic-tiles
# Y=550
# X1 = 800
# X2 = 900
# X3 = 1000
# X4 = 1100
# Black = 000





async def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


while keyboard.is_pressed('q') == False:

    if pyautogui.pixel(800,550)[0] == 0:
        asyncio.run(click(800,550))
    if pyautogui.pixel(900,550)[0] == 0:
        asyncio.run(click(900,550))
    if pyautogui.pixel(1000,550)[0] == 0:
        asyncio.run(click(1000,550))
    if pyautogui.pixel(1100,550)[0] == 0:
        asyncio.run(click(1100,550))
        
