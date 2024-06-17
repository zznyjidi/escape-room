from module.LevelDescriber import LevelDescriber
from module.LevelObject import img
from module.LevelBuilder import PlaceHolder as PH
import tkinter.messagebox
import config.drawing

LEVEL = LevelDescriber(NextLevelPos=(3, 4), RequireUnlock=False)
LEVEL_LOCKED = LevelDescriber(NextLevelPos=(3, 4), RequireUnlock=True)

TEST_IMG = img("assets/VERYIMPORTANT.png", (config.drawing.gridBlockSize, config.drawing.gridBlockSize), LEVEL_LOCKED.unlock)

DESCRIBER = [
    [TEST_IMG, PH.SPAWN, TEST_IMG,  TEST_IMG], 
    [TEST_IMG, None,     None,      TEST_IMG],
    [TEST_IMG, TEST_IMG, None,      TEST_IMG]
]

LEVEL.setDescriber(DESCRIBER[:])
LEVEL_LOCKED.setDescriber(DESCRIBER[:])

def doorLockedPopup():
    tkinter.messagebox.showinfo("DOOR", "The Door is Locked! ")

LEVEL_LOCKED.setLockedFunction(doorLockedPopup)
