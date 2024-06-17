from module.TileLoader import TileLoader
from module.LevelBuilder import LevelBuilder, PlaceHolder
from module.VirtualGrid import RelativePosition
from LevelObject import LevelObject
from typing import List, Tuple
from PIL import ImageTk
import config.drawing
import ttkbootstrap as ttk
import time

class MoveableObject:
    def move(self, angle: List[str]):
        """
        #### Move the Object. 

        Args:
            angle (List[str]): Angle to Move. (LEFT, RIGHT, UP, DOWN)
        """
        self.lastMove: List[str] = angle

    def interact(self):
        """
        #### Interact with nearby Object. 
        """

    def isMoveable(self) -> bool:
        """
        #### The Object is currently Moveable. 

        Returns:
            bool: Is Moveable. 
        """
        return True

class Player(MoveableObject):
    def __init__(self, master: LevelBuilder, tiles: TileLoader, debug: bool = False):
        """
        #### Create a Player Object. 

        Args:
            master (LevelBuilder): Level Builder to Add the Player. 
            tiles (TileLoader): Tiles to Use for the Character. 
            debug (bool, optional): Run in debug Mode. Defaults to False.
        """
        self.__debug = debug
        self.master = master
        self.tiles = tiles
        self.lastMove = ["DOWN"]

    def drawOnCanvas(self, location: Tuple[int, int]):
        """
        #### Add Object to Canvas. 

        Args:
            location (Tuple[int, int]): Location to add player. 
        """
        self.currentPos = list(location)
        self.currentFrameIndex: int = 0
        self.currentFrame = ImageTk.PhotoImage(self.tiles.getTile(config.drawing.tileConfig["STAND_DOWN"]))
        locationY, locationX = self.master.getBlockCoordinate(self.currentPos[1], self.currentPos[0], RelativePosition.CENTER)
        self.canvasImage = self.master.canvas.create_image(locationX, locationY, anchor=ttk.CENTER, image=self.currentFrame)

    def move(self, angle: List[str]):
        """
        #### Move the Player Object. 

        Args:
            angle (List[str]): Angle to Move. (LEFT, RIGHT, UP, DOWN)
        """
        super().move(angle)
        deltaX, deltaY = self.getBlockDelta(angle)

        if (deltaX != 0) or (deltaY != 0):
            self.currentFrameIndex += 1
            currentTileIndex = config.drawing.tileConfig[f"WALK_{angle[0]}_START"]
            if currentTileIndex[1] + self.currentFrameIndex > config.drawing.tileConfig[f"WALK_{angle[0]}_STOP"][1]:
                self.currentFrameIndex = 0
            self.currentFrame = ImageTk.PhotoImage(self.tiles.getTile((currentTileIndex[0], currentTileIndex[1] + self.currentFrameIndex)))
            self.master.canvas.itemconfig(self.canvasImage, image=self.currentFrame)
        
        if not self.master.haveHitBox(self.getPosFromDelta(deltaX, deltaY)):
            self.currentPos[0] += deltaX
            self.currentPos[1] += deltaY
            self.master.canvas.move(self.canvasImage, deltaX*config.drawing.gridBlockSize, deltaY*config.drawing.gridBlockSize)
        else:
            self.debugPrint(f"Collision in ({deltaX}, {deltaY}) From {self.currentPos}. Not Moving. ")

    def isInteractive(self, object: LevelObject | PlaceHolder | None = None) -> bool:
        """
        #### Check if Target Object is Interactive. 

        Args:
            object (LevelObject | PlaceHolder | None, optional): Object to Check. Defaults to None(Check Pointed Item). 

        Returns:
            bool: Target Object is Interactive. 
        """
        targetObject = (object if object != None else self.getPointedItem())
        if not isinstance(targetObject, LevelObject):
            return False
        if not targetObject.isInteractive():
            return False
        return True

    def interact(self):
        """
        #### Interact with Target Object. 
        """
        targetObject = self.getPointedItem()
        if not self.isInteractive(targetObject):
            self.debugPrint(f"Trying to Interact with Non-interactive Object {targetObject}. Did nothing. ")
        targetObject.interactive()()

    def getBlockDelta(self, angle: List[str]) -> Tuple[int, int]:
        """
        #### Calculate Delta Value based on Angles. 

        Args:
            angle (List[str]): Relative Angle from Current Place. 

        Returns:
            Tuple[int, int]: Difference in Block. (DeltaX, DeltaY)
        """
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
        return (deltaX, deltaY)

    def getPosFromDelta(self, delta: Tuple[int, int]) -> Tuple[int, int]:
        """
        #### Get Position from Delta. 

        Args:
            delta (Tuple[int, int]): Delta from Current Block. 

        Returns:
            Tuple[int, int]: Block After Delta. 
        """
        return (self.currentPos[0] + delta[0], self.currentPos[1] + delta[1])

    def getPointedItem(self) -> LevelObject | PlaceHolder | None:
        """
        #### Get Item that the Player is Facing. 

        Returns:
            LevelObject | PlaceHolder | None: Object that is Facing. 
        """
        return self.master.getItem(self.getPosFromDelta(self.getBlockDelta(self.lastMove)))

    def debugPrint(self, message):
        """
        #### Print if in Debug Mode. 

        Args:
            message: Message to Print. 
        """
        print(f"[{time.asctime()}][MoveableObject] {message}") if self.__debug else None
