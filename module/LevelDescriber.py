from module.LevelBuilder import PlaceHolder, wrapWithBoarder
from module.LevelObject import LevelObject
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
        self.NEXT_LEVEL = NextLevelPos
        self.UNLOCKED = not RequireUnlock

    def setDescriber(self, Describer: List[List[LevelObject | PlaceHolder | None]], wrap: bool=True):
        self.DESCRIBER = []
        for row in Describer:
            self.DESCRIBER.append(row[:])

        self.HEIGHT = len(self.DESCRIBER)
        self.WIDTH = len(self.DESCRIBER[0])
        if wrap:
            wrapWithBoarder(self.DESCRIBER)
            self.HEIGHT += 2
            self.WIDTH += 2
        self.GRID = VirtualGrid(self.HEIGHT, self.WIDTH, debug=True)
        self.GRID.importGrid(self.DESCRIBER)

    def setLockedFunction(self, func: Callable[[None], None]):
        self.LOCKED = func

    def lock(self):
        self.UNLOCKED = False

    def unlock(self):
        self.UNLOCKED = True
