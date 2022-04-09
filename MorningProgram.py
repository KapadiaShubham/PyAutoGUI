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

def Spotlight(what):
        pg.moveTo(0,57)
        sleep(0.5)
        pg.click()
        sleep(1)
        pg.keyDown("command")
        pg.press("space")
        pg.keyUp("command")
        sleep(0.3)
        pg.typewrite(what)
        sleep(0.5)
        pg.typewrite(["enter"])
        sleep(1.5)
    

def openSheet(which):
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
    

    # print (pg.position())  # 0,57
    Spotlight('Sheets')

    pg.hotkey("command", "option", "f")
    sleep(2)
    pg.click(430,95)
    sleep(0.5)
    pg.typewrite(which)
    sleep(2.5)
    pg.click(449,186)
    sleep(3)
    pg.click(760,881)
    pg.hotkey("option", "command", "left")

def openAnyChrome(which):
    which = 'chr'+which
    allchr = ['chrIITKGP','chrShubham']
    Spotlight('chr')
    pg.click(225, 87)
    pg.hotkey("option","command", "f")
    def gotoLogo(logo):
        x,y = logo
        print(x/2,y/2)
        pg.moveTo(x/2,y/2)
        
    logo = pg.locateCenterOnScreen(f'./logo/{which}.png')
    if(logo==None):
        allchr.remove(which)
        logo = pg.locateCenterOnScreen(f'./logo/{allchr[0]}.png')
        gotoLogo(logo)
        pg.click()
        sleep(0.2)
        if(which=='chrIITKGP'):
            pg.click(1181,650)
        elif(which=='chrShubham'):
            pg.click(1185,777)
    sleep(0.5)
    pg.click(113,50)
            