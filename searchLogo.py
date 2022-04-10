import pyautogui as pg
from functions import *

pg.click(225, 87)
# pg.hotkey("option","command", "f")
# logo[:] = [x / 2 for x in logo]
# x,y = logo
# PointToList(logo)
# print()
def gotoLogo(logo):
    x,y = logo
    print(x/2,y/2)
    pg.moveTo(x/2,y/2)
    
    
logo = pg.locateCenterOnScreen(f'./logo/downloadAttendance.png', grayscale=True) # a four-integer tuple of the left, top, width, and height of the region
gotoLogo(logo)
pg.click()
sleep(1)
pg.press("enter")