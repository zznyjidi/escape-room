import ttkbootstrap as ttk
from typing import Tuple, Union
from enum import StrEnum
from module.VirtualGrid import VirtualGrid, RelativePosition
from module.LevelObject import *

class PlaceHolder(StrEnum):
    IMAGE_LAST_LEVEL_TL = "IMAGE_LAST_LEVEL_TOP_LEFT"
    IMAGE_LAST_LEVEL_BR = "IMAGE_LAST_LEVEL_BOTTOM_RIGHT"
    COLLISION_TRIGGER = "COLLISION_TRIGGER"

class LevelBuilder(ttk.Frame):
    __items = {}

    def __init__(self, master):
        """
        #### Create a ttk Canvas that can Generate Game Level based on a Level Describer File. 

        Args:
            master: Master Object of the Frame that Contains the Canvas. 
        """
        super().__init__(master)
        self.canvas = ttk.Canvas(self)
        self.canvas.pack(fill='both', expand=True)

    def loadLevel(self, level: VirtualGrid):
        """
        #### Load the Level Describer. 

        Args:
            level (VirtualGrid): A VirtualGrid that Describe the Level. 
        """
        self.__currentLevel = level

    def saveLevel(self) -> VirtualGrid:
        """
        #### Save the Level Describer. 

        Returns:
            VirtualGrid: A VirtualGrid that Describe the Level.
        """
        return self.__currentLevel

    def haveItem(self, index: Tuple[int, int]) -> bool:
        """
        #### Check if there is a item in the specified position. 

        Args:
            index (Tuple[int, int]): Position to Check fro item. (Row, Col)

        Returns:
            bool: Have Item in specified position. 
        """
        return self.__currentLevel.haveItem(index[0], index[1]) != None

    def buildLevel(self):
        """
        #### Build Level with Loaded Level Describer. 
        """
        level: VirtualGrid = self.__currentLevel
        levelSize: Tuple[int, int] = level.size()
        for x in range(levelSize[0]):
            for y in range(levelSize[1]):
                item: Union[None, str, LevelObject] = level.getItem(x, y)
                itemCoordinate = level.getCoordinate(x, y, RelativePosition.TOP | RelativePosition.LEFT)
                if not issubclass(type(item), LevelObject):
                    continue
                self.__items[f"{item.getObjectType()}_{x}_{y}"] = item.addToCanvas(self.canvas, itemCoordinate)

    def clearLevel(self):
        """
        #### Remove All Elements From the Canvas. 
        """
        self.canvas.delete("all")
