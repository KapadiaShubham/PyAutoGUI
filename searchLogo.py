import pyautogui as pg
from functions import *

# logo = PointToList(pg.locateCenterOnScreen('myTeams.png'))
logo = pg.locateCenterOnScreen('myTeams.png')
# logo[:] = [x / 2 for x in logo]
# x,y = logo
# PointToList(logo)
# print()
print(logo)
# pg.moveTo(logo[0],logo[1])