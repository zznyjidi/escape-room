from module.TileLoader import TileLoader
from module.LevelBuilder import LevelBuilder
from module.VirtualGrid import RelativePosition
from typing import List, Tuple
from PIL import ImageTk
import config.drawing
import ttkbootstrap as ttk
import time

class MoveableObject:
    __debug = False

    def move(self, angle: List[str]):
        self.lastMove: List[str] = angle

    def isMoveable(self) -> bool:
        return True

class Player(MoveableObject):
    def __init__(self, master: LevelBuilder, tiles: TileLoader, defaultLocation: Tuple[int, int], debug: bool = False):
        self.__debug = debug
        self.master = master
        self.tiles = tiles
        self.currentPos = list(defaultLocation)
        self.currentFrameIndex: int = 0
        self.currentFrame = ImageTk.PhotoImage(tiles.getTile(config.drawing.tileConfig["STAND_DOWN"]))
        locationY, locationX = master.getBlockCoordinate(self.currentPos[1], self.currentPos[0], RelativePosition.CENTER)
        self.canvasImage = master.canvas.create_image(locationX, locationY, anchor=ttk.CENTER, image=self.currentFrame)

    def move(self, angle: List[str]):
        deltaX = 0
        deltaY = 0
        if "LEFT" in angle:
            deltaX -= 1
        if "RIGHT" in angle:
            deltaX += 1
        if "UP" in angle:
            deltaY -= 1
        if "DOWN" in angle:
            deltaY += 1

        if (deltaX != 0) or (deltaY != 0):
            self.currentFrameIndex += 1
            currentTileIndex = config.drawing.tileConfig[f"WALK_{angle[0]}_START"]
            if currentTileIndex[1] + self.currentFrameIndex > config.drawing.tileConfig[f"WALK_{angle[0]}_STOP"][1]:
                self.currentFrameIndex = 0
            self.currentFrame = ImageTk.PhotoImage(self.tiles.getTile((currentTileIndex[0], currentTileIndex[1] + self.currentFrameIndex)))
            self.master.canvas.itemconfig(self.canvasImage, image=self.currentFrame)
        
        if not self.master.haveHitBox((self.currentPos[0] + deltaX, self.currentPos[1] + deltaY)):
            self.currentPos[0] += deltaX
            self.currentPos[1] += deltaY
            self.master.canvas.move(self.canvasImage, deltaX*config.drawing.gridBlockSize, deltaY*config.drawing.gridBlockSize)
        else:
            self.debugPrint(f"Collision in ({deltaX}, {deltaY}) From {self.currentPos}.  Not Moving. ")

    def debugPrint(self, message):
        """
        #### Print if in Debug Mode. 

        Args:
            message: Message to Print. 
        """
        print(f"[{time.asctime()}][MoveableObject] {message}") if self.__debug else None
