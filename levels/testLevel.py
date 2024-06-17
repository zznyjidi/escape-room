from module.LevelDescriber import LevelDescriber
from module.LevelObject import img
from module.VirtualGrid import VirtualGrid
from module.LevelBuilder import PlaceHolder as PH, wrapWithBoarder
import config.drawing

LEVEL = LevelDescriber(NextLevelPos=(3, 4), RequireUnlock=False)
LEVEL_LOCKED = LevelDescriber(NextLevelPos=(3, 4), RequireUnlock=True)

TEST_IMG = img("assets/VERYIMPORTANT.png", (config.drawing.gridBlockSize, config.drawing.gridBlockSize))

DESCRIBER = [
    [TEST_IMG, PH.SPAWN, TEST_IMG,  TEST_IMG], 
    [TEST_IMG, None,     None,      TEST_IMG],
    [TEST_IMG, TEST_IMG, None,      TEST_IMG]
]

LEVEL.setDescriber(DESCRIBER[:])
LEVEL_LOCKED.setDescriber(DESCRIBER[:])
