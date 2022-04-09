# MAKE SURE FULL SCREEN
import pyautogui as pg
import pyperclip
# from functions import *
# whatYouCanOpen = ["teams", "NYSteams", "chrShubham", "chrLML","yt", "mmc"]
from time import sleep
# open -a "Microsoft Teams"     # COPY THIS

def openAnyTeams(what):
    # def optCmdF():
    #     pg.keyDown("option")
    #     pg.keyDown("command")
    #     pg.press("f")
    #     pg.keyUp("command")
    #     pg.keyUp("option")
        # pg.hotkey("command", "option", "f")
    # def Spotlight():
    #     pg.moveTo(0,57)
    #     sleep(0.5)
    #     pg.click()
    #     sleep(1)
    #     pg.keyDown("command")
    #     pg.press("space")
    #     pg.keyUp("command")
    #     sleep(0.3)
    #     pg.typewrite('Sheets')
    #     sleep(0.5)
    #     pg.typewrite(["enter"])
    #     sleep(1.5)

    def paste():
        pg.keyDown("command")
        pg.press("v")
        pg.keyUp("command")
    # print (pg.position())  # 0,57
    # Spotlight()

    # pg.hotkey("command", "option", "f")
    # sleep(2)
    # pg.click(430,95)
    # sleep(0.5)
    # pg.typewrite('MMC Attendance & Schedule')
    # sleep(2.5)
    # pg.click(449,186)
    # sleep(3)
    # pg.click(760,881)
    # pg.hotkey("option", "command", "left")
    # sleep(0.5)
    # pg.click(500,500)
    # pg.click(500,500)
    # pg.keyDown("command")
    # pg.press("c")
    # pg.keyUp("command")

    # sleep(0.5)
    pg.moveTo(0,83)
    sleep(0.5)
    pg.click()
    sleep(1)
    pyperclip.copy('open -a \"Microsoft Teams\"')
    paste()
    pg.press("enter")
    logo = pg.locateCenterOnScreen('./logo/teamsSearch.png')
    if(logo==None):
        sleep(1)
        
    pg.moveTo(443,49)
    pg.click()
    sleep(0.5)
    pyperclip.copy(what)
    paste()

    sleep(1.5)
    pg.moveTo(473,165) # teams after search
    pg.click()
    sleep(2)
    pg.moveTo(774,662) # Meet link
    pg.click()
    sleep(1)
    pg.moveTo(1307,105) # Join
    pg.click()
    sleep(1)
    logo = pg.locateCenterOnScreen('./logo/teamsMic.png')
    while(logo!=None):
        x,y = logo
        pg.moveTo((x/2)+4,y/2)
        pg.click()
        logo = pg.locateCenterOnScreen('./logo/teamsMic.png')

    # pg.hotkey("command", "space")
    # sleep(2)
    # pg.typewrite(["enter"])
    # sleep(2)

    # s = "open -a \"Microsoft Teams\""
    # s2 = "open -a \"Microsoft Teams\""
    # for char in s:
    #     pg.typewrite([char])

    # pg.typewrite('\"Microsoft Teams\"')

def open(what):
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
    pg.typewrite(what)
    sleep(2.5)
    pg.click(449,186)
    sleep(3)
    pg.click(760,881)
    pg.hotkey("option", "command", "left")

