from typing import List, Tuple
from module.LevelObject import LevelObject
from enum import IntEnum
import time, warnings

class RelativePosition(IntEnum):
    CENTER = 0b0000
    TOP = 0b1000
    BOTTOM = 0b0100
    LEFT = 0b0010
    RIGHT = 0b0001

class VirtualGrid:
    def __init__(self, rows: int, cols: int, sideLength: int = 1, debug: bool = False):
        """
        #### Create a Grid that is {rows} height and {cols} wide. 

        Args:
            rows (int): The height of the grid. 
            cols (int): The width of the grid. 
            sideLength (int): The side length of each element (square) in the grid. 
            debug (bool, optional): Debug Mode. Defaults to False.
        """
        self.__debug: bool = debug
        self.__size: Tuple[int, int] = (rows, cols)
        self.sideLength: int = sideLength
        self.__items: List[List[LevelObject]] = []
        for _ in range(rows):
            self.__items.append([None] * cols)

    def importGrid(self, newGrid: List[List[LevelObject]]):
        """
        #### Import a Grid From a 2D List. 

        Args:
            newGrid (List[List[LevelObject]]): 2D List that defines the Grid. 
        """
        self.__items = newGrid
        self.__size = (len(newGrid), len(newGrid[0]))
        self.debugPrint(f"New Grid Imported, Size: {self.__size}. \n{newGrid}")

    def exportGrid(self) -> List[List[LevelObject]]:
        """
        #### Export the Grid to a 2D List. 

        Returns:
            List[List[LevelObject]]: 2D List that defines the Grid. 
        """
        return self.__items

    def addItem(self, row: int, col: int, item: LevelObject, *, overwrite: bool = False):
        """
        #### Add item to Grid. 

        Args:
            row (int): Item position: Row. 
            col (int): Item position: Column. 
            item (LevelObject): Item to Add to the grid. 
            overwrite (bool, optional): Overwrite if the position already have a item. Defaults to False.
        """
        if (self.__items[row][col] != None):
            self.debugPrint(f"Overwriting a item in {row}, {col}. Original: {item}")
            if (not overwrite):
                warnings.warn(f"Trying to Overwrite {row}, {col} without specify overwrite, item not updated. ")
                return
        try:
            self.__items[row][col] = item
            self.debugPrint(f"Item {item} added to {row}, {col}. ")
        except IndexError:
            warnings.warn(f"Trying to Add item to index out of the grid {row}, {col}, item not updated. ")

    def removeItem(self, row: int, col: int):
        """
        #### Remove a item from Grid. 

        Args:
            row (int): Item position: Row. 
            col (int): Item position: Column. 
        """
        try:
            self.__items[row][col] = None
            self.debugPrint(f"Item removed from {row}, {col}. ")
        except IndexError:
            warnings.warn(f"Trying to Remove item to index out of the grid {row}, {col}, item not updated. ")

    def haveItem(self, row: int, col: int) -> bool:
        """
        #### Check if have item on index. 

        Args:
            row (int): Item position: Row. 
            col (int): Item position: Column. 

        Returns:
            bool: Have item on position. 
        """
        try:
            return self.__items[row][col] != None
        except IndexError:
            warnings.warn(f"Trying to check a index out of the grid {row}, {col}. ")
            return False

    def getItem(self, row: int, col: int) -> LevelObject:
        """
        #### Get a Item from the Grid. 

        Args:
            row (int): Item position: Row. 
            col (int): Item position: Column. 

        Returns:
            LevelObject: Item on the position. 
        """
        try:
            return self.__items[row][col]
        except IndexError:
            warnings.warn(f"Trying to get a item from a index out of the grid {row}, {col}, Returning None. ")
            return None

    def getCoordinate(self, row: int, col: int, point: RelativePosition) -> Tuple[int, int]:
        """
        #### Get position of element base on Index

        Args:
            row (int): Item position: Row. 
            col (int): Item position: Column. 
            point (RelativePosition): Position in the Block. Use multiple Position with | operator. 

        Returns:
            Tuple[int, int]: Relative Position to top left of the grid of the Item in Grid. 
        """
        if (len(self.__items) <= row) or (len(self.__items[0]) <= col):
            warnings.warn(f"Trying to get Coordinate of item from a index out of the grid {row}, {col}, Returning -1. ")
            return (-1, -1)
        rowPos: int = row * self.sideLength
        colPos: int = col * self.sideLength
        if int(format((point ^ RelativePosition.LEFT), "#06b")[4]):
            rowPos += self.sideLength/2
        if int(format((point ^ RelativePosition.TOP), "#06b")[2]):
            colPos += self.sideLength/2
        if not int(format((point ^ RelativePosition.RIGHT), "#06b")[5]):
            rowPos += self.sideLength/2
        if not int(format((point ^ RelativePosition.BOTTOM), "#06b")[3]):
            colPos += self.sideLength/2
        return (int(rowPos), int(colPos))

    def size(self) -> Tuple[int, int]:
        """
        #### Get the size of the Grid .

        Returns:
            Tuple[int, int]: Size of the Grid (Height, Width). 
        """
        return self.__size

    def pixelSize(self) -> Tuple[int, int]:
        """
        #### Get the size of the Grid in Pixel using sideLength. 

        Returns:
            Tuple[int, int]: Size of the Grid in Pixel. (Height, Width)
        """
        return tuple(map(lambda size: size * self.sideLength, self.__size))

    def debugPrint(self, message):
        """
        #### Print if in Debug Mode. 

        Args:
            message: Message to Print. 
        """
        print(f"[{time.asctime()}][VirtualGrid] {message}") if self.__debug else None

    def __getitem__(self, index: int) -> List[LevelObject]:
        """
        #### Access Items inside the virtual grid. 

        Args:
            index (int): Index of the Row. 

        Returns:
            List[LevelObject]: Items inside the Row. 
        """
        return self.__items[index]
