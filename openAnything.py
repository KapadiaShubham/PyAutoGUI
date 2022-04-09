
import pyautogui as pg
whatYouCanOpen = ["teams", "NYSteams", "chrShubham", "chrLML","yt", "mmc"]
open = ["yt"]
# open = ["NYSteams"]

pg.click(225, 87)
if open.count("yt") == 1:
    pg.typewrite("youtube.com")
    pg.typewrite(["enter"])
# pg.hotkey("command", "space")
if open.count("teams") == 1:
    pg.typewrite("Microsoft Teams")
    pg.typewrite(["enter"])
# pg.hotkey("command", "tab")
if open.count("NYSteams") == 1:
    pg.typewrite("NYS Microsoft Teams")
    pg.typewrite(["enter"])

