# MAKE SURE FULL SCREEN
import pyautogui as pg
# from functions import *
# whatYouCanOpen = ["teams", "NYSteams", "chrShubham", "chrLML","yt", "mmc"]
from time import sleep
# open -a "Microsoft Teams"     # COPY THIS
def copyCmd():    
    pg.click(777,437)
    pg.hotkey("command", "up")
    for i in range(5):
        pg.press("down")
    for i in range(5):
        pg.press("right")
    pg.keyDown("shift")
    for i in range(len(s)):
        pg.press("right")
    pg.keyUp("shift")
    pg.hotkey("command", "c")

# copyCmd()
open = ["mmc"]


def optCmdF():
    pg.keyDown("option")
    pg.keyDown("command")
    pg.press("f")
    pg.keyUp("command")
    pg.keyUp("option")
    # pg.hotkey("command", "option", "f")
def Spotlight():
    pg.moveTo(0,57)
    sleep(0.5)
    pg.click()
    sleep(1)
    pg.keyDown("command")
    pg.press("space")
    pg.keyUp("command")
    sleep(0.3)
    pg.typewrite('Sheets')
    sleep(0.5)
    pg.typewrite(["enter"])
    sleep(1.5)

# print (pg.position())  # 0,57
Spotlight()

pg.hotkey("command", "option", "f")
sleep(2)
pg.click(430,95)
sleep(0.5)
pg.typewrite('MMC Attendance & Schedule')
sleep(2.5)
pg.click(449,186)
sleep(3)
pg.click(760,881)
pg.hotkey("option", "command", "left")

sleep(0.5)
pg.moveTo(0,83)
sleep(0.5)
pg.click()
sleep(1)

pg.keyDown("command")
pg.press("v")
pg.keyUp("command")
pg.press("enter")
sleep(10)
pg.moveTo(443,49)
pg.click()

# pg.hotkey("command", "space")
# sleep(2)
# pg.typewrite('Terminal')
# pg.typewrite(["enter"])
# sleep(2)

# s = "open -a \"Microsoft Teams\""
# s2 = "open -a \"Microsoft Teams\""
# for char in s:
#     pg.typewrite([char])

# pg.typewrite('\"Microsoft Teams\"')



