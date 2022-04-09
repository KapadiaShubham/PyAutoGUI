import pyautogui as pg
from functions import *

pg.click(225, 87)
pg.hotkey("option","command", "f")
# logo[:] = [x / 2 for x in logo]
# x,y = logo
# PointToList(logo)
# print()
def gotoLogo(logo):
    x,y = logo
    print(x/2,y/2)
    pg.moveTo(x/2,y/2)
    
    
logo = pg.locateCenterOnScreen('./logo/chrShubham.png')
if(logo!=None):
    gotoLogo(logo)
    pg.click()
    sleep(0.2)
    pg.click(1181,650)
else:
    logo = pg.locateCenterOnScreen('./logo/chrIITKGP.png')
    if(logo!=None):
        gotoLogo(logo)
        pg.click()
        sleep(0.2)
        pg.click(1185,777)