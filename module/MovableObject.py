from module.TileLoader import TileLoader
from typing import List, Tuple
from PIL import ImageTk
import config.drawing
import ttkbootstrap as ttk

class MoveableObject:
    def move(self, angle: List[str]):
        self.lastMove: List[str] = angle

    def isMoveable(self) -> bool:
        return True

class Player(MoveableObject):
    def __init__(self, master: ttk.Canvas, tiles: TileLoader, defaultLocation: Tuple[int, int]):
        self.master = master
        self.tiles = tiles
        self.currentFrameIndex = 0
        self.currentFrame = ImageTk.PhotoImage(tiles.getTile(config.drawing.tileConfig["STAND_DOWN"]))
        self.canvasImage = master.create_image(defaultLocation[0], defaultLocation[1], anchor=ttk.CENTER, image=self.currentFrame)

    def move(self, angle: List[str]):
        deltaX = 0
        deltaY = 0
        if "LEFT" in angle:
            deltaX -= config.drawing.gridBlockSize
        if "RIGHT" in angle:
            deltaX += config.drawing.gridBlockSize
        if "UP" in angle:
            deltaY -= config.drawing.gridBlockSize
        if "DOWN" in angle:
            deltaY += config.drawing.gridBlockSize

        if (deltaX != 0) or (deltaY != 0):
            self.currentFrameIndex += 1
            currentTileIndex = config.drawing.tileConfig[f"WALK_{angle[0]}_START"]
            if currentTileIndex[1] + self.currentFrameIndex > config.drawing.tileConfig[f"WALK_{angle[0]}_STOP"][1]:
                self.currentFrameIndex = 0
            self.currentFrame = ImageTk.PhotoImage(self.tiles.getTile((currentTileIndex[0], currentTileIndex[1] + self.currentFrameIndex)))

        self.master.move(self.canvasImage, deltaX, deltaY)
        self.master.itemconfig(self.canvasImage, image=self.currentFrame)
