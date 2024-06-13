import ttkbootstrap as ttk
from typing import Tuple
from enum import StrEnum
from module.VirtualGrid import VirtualGrid, RelativePosition
from module.LevelObject import *

class PlaceHolder(StrEnum):
    IMAGE_LAST_LEVEL_TL = "IMAGE_LAST_LEVEL_TOP_LEFT"
    IMAGE_LAST_LEVEL_BR = "IMAGE_LAST_LEVEL_BOTTOM_RIGHT"
    COLLISION_TRIGGER = "COLLISION_TRIGGER"

class LevelBuilder(ttk.Frame):
    __items = {}
    __noPackItems = [None, PlaceHolder.IMAGE_LAST_LEVEL_TL, PlaceHolder.IMAGE_LAST_LEVEL_BR, PlaceHolder.COLLISION_TRIGGER]

    def __init__(self, master):
        super().__init__(master)
        self.__canvas = ttk.Canvas(self)
        self.__canvas.pack(fill='both', expand=True)

    def loadLevel(self, level: VirtualGrid):
        self.__currentLevel = level

    def saveLevel(self) -> VirtualGrid:
        return self.__currentLevel

    def haveItem(self, index: Tuple[int, int]) -> bool:
        return self.__currentLevel[index[0]][index[1]] != None

    def buildLevel(self):
        level: VirtualGrid = self.__currentLevel
        levelSize: Tuple[int, int] = level.size()
        for x in range(levelSize[0]):
            for y in range(levelSize[1]):
                item = level.getItem(x, y)
                itemCoordinate = level.getCoordinate(x, y, RelativePosition.TOP | RelativePosition.LEFT)
                if item in self.__noPackItems:
                    continue
                self.__items[f"{item.getObjectType()}_{x}_{y}"] = item.addToCanvas(self.__canvas, itemCoordinate)
