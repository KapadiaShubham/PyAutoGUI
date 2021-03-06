# MAKE SURE FULL SCREEN
from curses.ascii import SP
import pyautogui as pg
import pyperclip
# from functions import *
# whatYouCanOpen = ["teams", "NYSteams", "chrShubham", "chrLML","yt", "mmc"]
from time import sleep
# open -a "Microsoft Teams"     # COPY THIS

def paste():
        pg.keyDown("command")
        pg.press("v")
        pg.keyUp("command")
        
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
    while(logo==None):
        sleep(1)
        logo = pg.locateCenterOnScreen('./logo/teamsSearch.png')
        
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
    sleep(2)
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

def openAnyTeamsChat(what):
    pg.moveTo(0,83)
    sleep(0.5)
    pg.click()
    sleep(1)
    pyperclip.copy('open -a \"Microsoft Teams\"')
    paste()
    pg.press("enter")
    logo = pg.locateCenterOnScreen('./logo/teamsSearch.png')
    pg.hotkey("option","command", "f")
    while(logo==None):
        sleep(1)
        logo = pg.locateCenterOnScreen('./logo/teamsSearch.png')
        
    pg.moveTo(443,49)
    pg.click()
    sleep(0.5)
    pyperclip.copy(what)
    paste()

    sleep(1.5)
    pg.moveTo(473,165) # teams after search
    pg.click()

def Spotlight(what):
        pg.moveTo(0,57)
        sleep(0.5)
        pg.click()
        sleep(1)
        pg.keyDown("command")
        pg.press("space")
        pg.keyUp("command")
        sleep(0.3)
        pg.moveTo(200,200)
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

def gotoLogo(logo):
    x,y = logo
    print(x/2,y/2)
    pg.moveTo(x/2,y/2)
        
def openAnyChrome(which):
    Spotlight('chr')
    which = 'chr'+which
    allchr = ['chrIITKGP','chrShubham']
    sleep(5)
    pg.hotkey("option","command", "f")
    pg.click(225, 87)
    
        
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
            
def openBrave(link):
    Spotlight('brave')
    sleep(1)
    pyperclip.copy(link)
    pg.hotkey("option","command", "f")
    pg.click(350, 83)
    paste()
    pg.press("enter")
    
def mmcAttendance():
    Spotlight('NYS Microsoft Teams')
    sleep(5)
    pg.hotkey("option","command", "f")
    pg.click(1422,872)
    pg.click(486,311)
    sleep(1)
    logo = pg.locateCenterOnScreen(f'./logo/downloadAttendance.png', grayscale=True) # a four-integer tuple of the left, top, width, and height of the region
    gotoLogo(logo)
    pg.click()
    sleep(1.5)
    pg.typewrite(["enter"])
    sleep(0.1)
    pg.hotkey("option","command", "right")
    sleep(0.1)
    openAnyTeamsChat('MMC Attendance')
    pg.hotkey("option","command", "left")
    pg.moveTo(0,720)
    sleep(0.3)
    pg.moveTo(20,720)
    pg.click()
    # drag to 590, 840
    
    # 537, 662
    # 621, 740
def playMusic(number):
    logo = pg.locateCenterOnScreen(f'./logo/playMusic.png', grayscale=True)
    gotoLogo(logo)
    pg.click()
    sleep(0.3)
    logo = pg.locateCenterOnScreen(f'./logo/nextMusic.png', grayscale=True)
    gotoLogo(logo)
    pg.click(clicks=number-1, interval=0.25)
    
    
def repo(which):
    sleep(1)
    pg.click(250, 40)
    sleep(0.3)
    logo = pg.locateCenterOnScreen(f'./logo/dropdownRepos.png', grayscale=True) 
    if(logo):
        gotoLogo(logo)
        pg.click()
    
    logo = pg.locateCenterOnScreen(f'./logo/{which}1.png', grayscale=True) 
    if(logo):
        gotoLogo(logo)
    else:
        logo = logo = pg.locateCenterOnScreen(f'./logo/{which}2.png', grayscale=True) 
        gotoLogo(logo)
    pg.click()
    sleep(1)
    pg.keyDown('command')
    pg.keyDown('shift')
    pg.press('a')
    pg.keyUp('shift')
    pg.keyUp('command')
    # hotkey("shift","command","a")
    
def SpotlightMultiple(*argv):
    for arg in argv:
        Spotlight(arg)

def chrNewTab(link):
    pg.hotkey("command", "t")
    pyperclip.copy(link)
    paste()
    pg.press("enter")

def spectackleDisUnable():
    logo = pg.locateCenterOnScreen(f'./logo/spectackle.png', grayscale=True) 
    if(logo):
        gotoLogo(logo)
        pg.click()
        x,y = logo
        x/=2
        y/=2
        pg.moveTo(x,y+85)
        sleep(0.5)
        pg.moveTo(x+220,y+85)
        pg.click()
        sleep(0.2)

def fillSadhanaCard():
    openAnyChrome('Shubham')
    sleep(1)
    chrNewTab('https://docs.google.com/spreadsheets/d/1E-PXwdOztF2fu6tiU-k8QXbSkhJMZ9fJQoQmMPRknek/edit#gid=308003546')
    

def mailSadhanaCard():
    fillSadhanaCard()
    chrNewTab('https://mail.google.com/mail/u/0/#inbox')
    sleep(1)
    spectackleDisUnable()
    