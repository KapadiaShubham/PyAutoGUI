import pyautogui as pg
import pyperclip
from time import sleep

def scroll():
    pg.moveTo(220,270)
    for s in range(10):
        pg.scroll(-1)
        sleep(0.1)
    

n = 4
while(n):
    n-=1
    logo = pg.locateAllOnScreen('./logo/TelNewChat.png')
    for pos in logo:
        print(pos)
    scroll()
