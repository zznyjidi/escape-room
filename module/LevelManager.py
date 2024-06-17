from module.VirtualGrid import VirtualGrid
from module.LevelBuilder import LevelBuilder, PlaceHolder
from module.LevelObject import interact
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
        self.levelGrids: List[VirtualGrid] = []
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

        self.levelBuilder.loadLevel(self.levelGrids[self.currentLevel])
        self.levelBuilder.buildLevel()
        self.playerObject.drawOnCanvas(self.levelBuilder.param[PlaceHolder.SPAWN])
        self.playerController.attachPlayer(self.playerObject)

        self.levelBuilder.pack(fill="both", expand=True)
        self.globalTimer.start() if not self.globalTimer is None else None

    def addTimer(self, timeSec: int):
        """
        #### Add a Timer to the Game. 

        Args:
            timeSec (int): Seconds that the Timer will have. 
        """
        self.globalTimer = timer(timeSec, lambda: self.failed("TIMER_END"), debug=self.__debug)

    def addLevel(self, level):
        """
        #### Add a Level to the Game. 

        Args:
            level (Module): Level Describer File. (See testLevel for Examples. )
        """
        self.levelGrids.append(level.LEVEL)
        self.levelGrids[-1].addItem(level.NEXT_LEVEL[1], level.NEXT_LEVEL[0], interact(self.nextLevel, True), overwrite=True)

    def addPlayerTiles(self, tiles: TileLoader):
        """
        #### Add Tiles for Player. 

        Args:
            tiles (TileLoader): New Tiles. 
        """
        self.playerTiles.append(tiles)

    def nextLevel(self):
        self.currentLevel += 1
        raise NotImplementedError

    def success(self):
        raise NotImplementedError

    def failed(self, reason):
        raise NotImplementedError
