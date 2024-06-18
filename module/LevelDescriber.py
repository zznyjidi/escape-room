from module.LevelBuilder import PlaceHolder, wrapWithBoarder
from module.LevelObject import LevelObject, img, interact
from module.VirtualGrid import VirtualGrid
from typing import List, Tuple, Callable

class LevelDescriber:
    GRID: VirtualGrid
    NEXT_LEVEL: Tuple[int, int]
    UNLOCKED: bool
    LOCKED: Callable[[None], None]
    DESCRIBER: List[List[LevelObject | PlaceHolder | None]]
    HEIGHT: int
    WIDTH: int

    def __init__(self, *, NextLevelPos: Tuple[int, int], RequireUnlock: bool=True):
        """
        #### Level Configs. 

        Args:
            NextLevelPos (Tuple[int, int]): Next Level Block. 
            RequireUnlock (bool, optional): Require Unlock to Go to Next Level. Defaults to True.
        """
        self.NEXT_LEVEL = NextLevelPos
        self.UNLOCKED = not RequireUnlock

    def setDescriber(self, Describer: List[List[LevelObject | PlaceHolder | None]], wrap: bool=True, nextLevelImg: img | None = None):
        """
        #### Set Level Describer for the Level. 

        Args:
            Describer (List[List[LevelObject  |  PlaceHolder  |  None]]): Level Describer. 
            wrap (bool, optional): Wrap Level with Hitbox. Defaults to True.
        """
        self.DESCRIBER = []
        for row in Describer:
            self.DESCRIBER.append(row[:])

        self.HEIGHT = len(self.DESCRIBER)
        self.WIDTH = len(self.DESCRIBER[0])
        if wrap:
            wrapWithBoarder(self.DESCRIBER)
            self.HEIGHT += 2
            self.WIDTH += 2
        if nextLevelImg is None:
            self.DESCRIBER[self.NEXT_LEVEL[1]][self.NEXT_LEVEL[0]] = interact(None, True)
        else:
            self.DESCRIBER[self.NEXT_LEVEL[1]][self.NEXT_LEVEL[0]] = nextLevelImg
        self.GRID = VirtualGrid(self.HEIGHT, self.WIDTH)
        self.GRID.importGrid(self.DESCRIBER)

    def setMaster(self, master):
        """
        #### Set the Level's Master Level Manager. 

        Args:
            master (LevelManager): The Game's LevelManager. 
        """
        self.MASTER = master

    def setLockedFunction(self, func: Callable[[None], None]):
        """
        #### Set Function to Run when Trying to Go to Next Level Without Unlock. 

        Args:
            func (Callable[[None], None]): Function to Run. 
        """
        self.LOCKED = func

    def lock(self):
        """
        #### Lock the Level. 
        """
        self.UNLOCKED = False

    def unlock(self):
        """
        #### Unlock the Level. 
        """
        self.UNLOCKED = True
