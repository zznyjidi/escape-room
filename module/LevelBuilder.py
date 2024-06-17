import ttkbootstrap as ttk
import pyscreenshot as ImageGrab
import time
from typing import List, Tuple, Union
from enum import StrEnum
from PIL import Image
from module.VirtualGrid import VirtualGrid, RelativePosition
from module.LevelObject import LevelObject

class PlaceHolder(StrEnum):
    LL_TL = "IMAGE_LAST_LEVEL_TOP_LEFT"
    LL_BR = "IMAGE_LAST_LEVEL_BOTTOM_RIGHT"
    HITBOX = "HITBOX"
    SPAWN = "SPAWN_POINT"

collisionItems = [PlaceHolder.LL_TL, PlaceHolder.LL_BR, PlaceHolder.HITBOX]
def wrapWithBoarder(levelDescriber: List[List[LevelObject | str | None]]):
    """
    #### Warp The Level Describer with HitBoxes. 

    Args:
        levelDescriber (List[List[LevelObject  |  str  |  None]]): Level Describer. 
    """
    for i in levelDescriber:
        i.insert(0, PlaceHolder.HITBOX)
        i.append(PlaceHolder.HITBOX)
    levelWidth = len(levelDescriber[0])
    levelDescriber.insert(0, [PlaceHolder.HITBOX]*levelWidth)
    levelDescriber.append([PlaceHolder.HITBOX]*levelWidth)

class LevelBuilder(ttk.Frame):
    __items = {}

    def __init__(self, master, debug: bool = False):
        """
        #### Create a ttk Canvas that can Generate Game Level based on a Level Describer File. 

        Args:
            master: Master Object of the Frame that Contains the Canvas. 
            debug (bool, optional): Run in debug Mode. Defaults to False.
        """
        self.__debug: bool = debug
        super().__init__(master)
        self.canvas = ttk.Canvas(self)
        self.canvas.pack(fill='none', expand=True)

    def loadLevel(self, level: VirtualGrid):
        """
        #### Load the Level Describer. 

        Args:
            level (VirtualGrid): A VirtualGrid that Describe the Level. 
        """
        self.__currentLevel = level
        self.debugPrint(f"New VirtualGrid {level} Loaded. ")

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
            index (Tuple[int, int]): Position to Check fro item. (X, Y)

        Returns:
            bool: Have Item in specified position. 
        """
        return not self.__currentLevel.haveItem(index[1], index[0]) is None

    def haveHitBox(self, index: Tuple[int, int]) -> bool:
        """
        #### Check if Collision will trigger on the given block. 

        Args:
            index (Tuple[int, int]): Block to check. 

        Returns:
            bool: Have collision. 
        """
        if not self.haveItem(index):
            return False
        item = self.__currentLevel.getItem(index[1], index[0])
        if item in collisionItems:
            return True
        if isinstance(item, LevelObject):
            return item.collision
        return False

    def getBlockCoordinate(self, row: int, col: int, point: RelativePosition) -> Tuple[int, int]:
        """
        #### Get Coordinate From Grid. 

        Args:
            row (int): Item position: Row. 
            col (int): Item position: Column. 
            point (RelativePosition): Position in the Block. Use multiple Position with | operator. 

        Returns:
            Tuple[int, int]: Relative Position to top left of the grid of the Item in Grid. 
        """
        return self.__currentLevel.getCoordinate(row, col, point)

    def buildLevel(self):
        """
        #### Build Level with Loaded Level Describer. 
        """
        level: VirtualGrid = self.__currentLevel
        levelSize: Tuple[int, int] = level.size()
        levelSizePixel: Tuple[int, int] = level.pixelSize()
        self.canvas.configure(width=levelSizePixel[1], height=levelSizePixel[0])
        for y in range(levelSize[0]):
            for x in range(levelSize[1]):
                item: Union[None, str, LevelObject] = level.getItem(y, x)
                itemCoordinate = level.getCoordinate(y, x, RelativePosition.CENTER)
                self.debugPrint(f"Item {item} Loaded From Grid {(x, y)}, at {itemCoordinate}. ")
                if not isinstance(item, LevelObject):
                    self.debugPrint(f"Unable to Add Item {item} to Canvas, Skipped. ")
                    continue
                self.__items[f"{item.getObjectType()}_{x}_{y}"] = item.addToCanvas(self.canvas, itemCoordinate)
                self.debugPrint(f"Item {item} Added to Canvas. ")
                self.getRootWindow().update()

    def clearLevel(self):
        """
        #### Remove All Elements From the Canvas. 
        """
        self.canvas.delete("all")
        self.debugPrint("Canvas is cleared. ")

    def toImage(self) -> Image:
        """
        #### Generate a Image Using the Canvas. 

        Returns:
            Image: Image of the Canvas. 
        """
        xStart = self.winfo_rootx()
        yStart = self.winfo_rooty()
        xStop = xStart + self.canvas.winfo_width()
        yStop = yStart + self.canvas.winfo_height()

        return ImageGrab.grab().crop((xStart, yStart, xStop, yStop))

    def getRootWindow(self) -> ttk.Window:
        """
        #### Get the Root Window of the Widget. 

        Returns:
            ttk.Window: Root Window. 
        """
        rootWindow = self
        while not rootWindow.master is None:
            rootWindow = rootWindow.master
        return rootWindow

    def debugPrint(self, message):
        """
        #### Print if in Debug Mode. 

        Args:
            message: Message to Print. 
        """
        print(f"[{time.asctime()}][LevelBuilder] {message}") if self.__debug else None
