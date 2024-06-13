import ttkbootstrap as ttk
from typing import Tuple
from enum import Enum
from module.VirtualGrid import VirtualGrid, RelativePosition

class PlaceHolder(Enum):
    IMAGE_LAST_LEVEL_TL = "IMAGE_LAST_LEVEL_TOP_LEFT"
    IMAGE_LAST_LEVEL_BR = "IMAGE_LAST_LEVEL_BOTTOM_RIGHT"
    COLLISION_TRIGGER = "COLLISION_TRIGGER"

class LevelBuilder(ttk.Frame):
    __items = {}
    def __init__(self, master):
        super().__init__(master)
        self.__canvas = ttk.Canvas(self)
        self.__canvas.pack(fill='both', expand=True)

    def loadLevel(self, level: VirtualGrid):
        self.__currentLevel = level

    def saveLevel(self) -> VirtualGrid:
        return self.__currentLevel

    def haveItem(self, index: Tuple[int, int]):
        self.__currentLevel[index[0]][index[1]]

    def buildLevel(self):
        level: VirtualGrid = self.__currentLevel
        levelSize: Tuple[int, int] = level.size()
        for x in range(levelSize[0]):
            for y in range(levelSize[1]):
                itemCoordinate = level.getCoordinate(x, y, RelativePosition.TOP | RelativePosition.LEFT)
                self.items[f"IMAGE_{x}_{y}"] = self.__canvas.create_image(itemCoordinate[0], itemCoordinate[1], anchor=ttk.NW, image=level.getItem(x, y))
