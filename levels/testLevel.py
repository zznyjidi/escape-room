from module.LevelObject import img
import config.drawing

TEST_IMG = img("assets/VERYIMPORTANT.png", (config.drawing.gridBlockSize, config.drawing.gridBlockSize))

describer = [
    [TEST_IMG, None,     TEST_IMG,  TEST_IMG], 
    [TEST_IMG, None,     None,      TEST_IMG],
    [TEST_IMG, TEST_IMG, None,      TEST_IMG]
]
