from module.LevelObject import img
from module.VirtualGrid import VirtualGrid
from module.LevelBuilder import PlaceHolder as PH, wrapWithBoarder
import config.drawing

TEST_IMG = img("assets/VERYIMPORTANT.png", (config.drawing.gridBlockSize, config.drawing.gridBlockSize))

NEXT_LEVEL = (3, 4)
DESCRIBER = [
    [TEST_IMG, PH.SPAWN, TEST_IMG,  TEST_IMG], 
    [TEST_IMG, None,     None,      TEST_IMG],
    [TEST_IMG, TEST_IMG, None,      TEST_IMG]
]

wrapWithBoarder(DESCRIBER)
LEVEL = VirtualGrid(5, 6)
LEVEL.importGrid(DESCRIBER)
