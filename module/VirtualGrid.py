from typing import List, Any
import time, warnings

class VirtualGrid:
    def __init__(self, rows: int, cols: int, debug: bool = False):
        """
        #### Create a Grid that is {rows} height and {cols} wide. 

        Args:
            rows (int): The height of the grid. 
            cols (int): The width of the grid. 
            debug (bool, optional): Debug Mode. Defaults to False.
        """
        self.__debug: bool = debug
        self.__items: List[List[Any]] = []
        for _ in range(rows):
            self.__items.append([None] * cols)

    def importGrid(self, newGrid: List[List[Any]]):
        """
        #### Import a Grid From a 2D List. 

        Args:
            newGrid (List[List[Any]]): 2D List that defines the Grid. 
        """
        self.__items = newGrid

    def exportGrid(self) -> List[List[Any]]:
        """
        #### Export the Grid to a 2D List. 

        Returns:
            List[List[Any]]: 2D List that defines the Grid. 
        """
        return self.__items

    def addItem(self, row: int, col: int, item: Any, *, overwrite: bool = False):
        """
        #### Add item to Grid. 

        Args:
            row (int): Item position: Row. 
            col (int): Item position: Column. 
            item (Any): Item to Add to the grid. 
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

    def getItem(self, row: int, col: int) -> Any:
        """
        #### Get a Item from the Grid. 

        Args:
            row (int): Item position: Row. 
            col (int): Item position: Column. 

        Returns:
            Any: Item on the position. 
        """
        try:
            return self.__items[row][col]
        except IndexError:
            warnings.warn(f"Trying to get a item from a index out of the grid {row}, {col}, Returning None. ")
            return None

    def debugPrint(self, message):
        """
        #### Print if in Debug Mode. 

        Args:
            message: Message to Print. 
        """
        print(f"[{time.asctime()}][VirtualGrid] {message}") if self.__debug else None

    def __getitem__(self, index: int) -> List[Any]:
        """
        #### Access Items inside the virtual grid. 

        Args:
            index (int): Index of the Row. 

        Returns:
            List[Any]: Items inside the Row. 
        """
        return self.__items[index]
