from PIL import Image, ImageTk
from ttkbootstrap import Canvas, NW
from typing import Tuple, Any

class LevelObject:
    objectType: str = "BASE"
    targetCanvas: Canvas
    targetCoordinate: Tuple[int, int]

    def addToCanvas(self, canvas: Canvas, coordinate: Tuple[int, int]):
        self.targetCanvas = canvas
        self.targetCoordinate = coordinate

    def getObjectType(self) -> str:
        return self.objectType

class img(LevelObject):
    def __init__(self, imgPath: str, size: Tuple[int, int]):
        self.objectType = "IMAGE"
        self.object: Image = Image.open(imgPath)
        self.object.thumbnail(size)

    def addToCanvas(self, canvas: Canvas, coordinate: Tuple[int, int]) -> Any:
        super().addToCanvas(canvas, coordinate)
        self.__PhotoImg = ImageTk.PhotoImage(self.object)
        return canvas.create_image(self.targetCoordinate, anchor=NW, image=self.__PhotoImg)
