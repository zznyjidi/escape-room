from module.LevelBuilder import LevelBuilder, PlaceHolder
from module.LevelObject import interact
from module.LevelDescriber import LevelDescriber
from module.MovableObject import Player
from module.GlobalTimer import timer
from module.TileLoader import TileLoader
from module.PlayerController import PlayerController
from typing import List
import tkinter as tk

class LevelManager:
    def __init__(self, debug: bool = False):
        """
        #### A Manager that Helps you Manager All Levels. 

        Args:
            debug (bool, optional): Run in Debug Mode. Defaults to False.
        """
        self.__debug = debug
        self.currentLevel = 0
        self.currentTiles = 0
        self.levels: List[LevelDescriber] = []
        self.playerTiles: List[TileLoader] = []
        self.globalTimer = None

    def initGame(self, master: tk.Misc):
        """
        #### Initialise the First Level and Pack the Frame. 

        Args:
            master (tk.Misc): Window/Frame to Pack the Game. 
        """
        self.levelBuilder = LevelBuilder(master, debug=self.__debug)
        self.playerController = PlayerController(master, debug=self.__debug)
        self.playerObject = Player(self.levelBuilder, self.playerTiles[self.currentTiles], debug=self.__debug)

        self.levelBuilder.pack(fill="both", expand=True)
        self.buildCurrentLevel()

        self.globalTimer.start() if not self.globalTimer is None else None

    def addTimer(self, timeSec: int):
        """
        #### Add a Timer to the Game. 

        Args:
            timeSec (int): Seconds that the Timer will have. 
        """
        self.globalTimer = timer(timeSec, lambda: self.failed("TIMER_END"), debug=self.__debug)

    def addLevel(self, *levels: LevelDescriber):
        """
        #### Add a Level to the Game. 

        Args:
            levels (Module): Level Describer File. (See testLevel for Examples. )
        """
        for level in levels:
            self.levels.append(level)
            self.levels[-1].GRID.addItem(level.NEXT_LEVEL[1], level.NEXT_LEVEL[0], interact(self.nextLevel, True), overwrite=True)
            self.levels[-1].setMaster(self)

    def addPlayerTiles(self, tiles: TileLoader):
        """
        #### Add Tiles for Player. 

        Args:
            tiles (TileLoader): New Tiles. 
        """
        self.playerTiles.append(tiles)

    def buildCurrentLevel(self):
        """
        #### Build Current Level. 
        """
        self.levelBuilder.loadLevel(self.levels[self.currentLevel].GRID)
        self.levelBuilder.buildLevel()
        self.playerObject.drawOnCanvas(self.levelBuilder.param[PlaceHolder.SPAWN])
        self.playerController.attachPlayer(self.playerObject)

    def nextLevel(self):
        """
        #### Go to Next Level if exist or to Success when Current Level is Unlocked. 
        Bind to NEXT_LEVEL by Default. 
        """
        if not self.levels[self.currentLevel].UNLOCKED:
            self.levels[self.currentLevel].LOCKED()
            return
        self.currentLevel += 1
        self.playerController.detachPlayer()
        self.levelBuilder.clearLevel()
        if self.currentLevel < len(self.levels):
            self.buildCurrentLevel()
        else:
            self.success()

    def success(self):
        raise NotImplementedError

    def failed(self, reason):
        raise NotImplementedError
