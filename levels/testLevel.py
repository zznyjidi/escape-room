from module.LevelObject import img
from module.VirtualGrid import VirtualGrid
from module.LevelBuilder import PlaceHolder as PH, wrapWithBoarder
import config.drawing

TEST_IMG = img("assets/VERYIMPORTANT.png", (config.drawing.gridBlockSize, config.drawing.gridBlockSize))

describer = [
    [TEST_IMG, PH.SPAWN, TEST_IMG,  TEST_IMG], 
    [TEST_IMG, None,     None,      TEST_IMG],
    [TEST_IMG, TEST_IMG, None,      TEST_IMG]
]

wrapWithBoarder(describer)
levelGrid = VirtualGrid(5, 6)
levelGrid.importGrid(describer)
