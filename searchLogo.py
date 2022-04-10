import pyautogui as pg
from functions import *

# pg.click(250, 40)
# pg.hotkey("option","command", "f")
# logo[:] = [x / 2 for x in logo]
# x,y = logo
# PointToList(logo)
# print()
def gotoLogo(logo):
    x,y = logo
    print(x/2,y/2)
    pg.moveTo(x/2,y/2)
    
    
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

