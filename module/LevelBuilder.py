import ttkbootstrap as ttk
from typing import Tuple
from module.VirtualGrid import VirtualGrid

class PlaceHolder:
    IMAGE_LAST_LEVEL_TL = "IMAGE_LAST_LEVEL_TOP_LEFT"
    IMAGE_LAST_LEVEL_BR = "IMAGE_LAST_LEVEL_BOTTOM_RIGHT"
    COLLISION_TRIGGER = "COLLISION_TRIGGER"

class LevelBuilder(ttk.Frame):
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
