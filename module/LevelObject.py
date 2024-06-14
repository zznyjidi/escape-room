from PIL import Image, ImageTk
from ttkbootstrap import Canvas, NW
from typing import Tuple, List, Any, Callable

class LevelObject:
    objectType: str = "BASE"
    targetCanvas: Canvas
    targetCoordinate: Tuple[int, int]

    def addToCanvas(self, canvas: Canvas, coordinate: Tuple[int, int]):
        self.targetCanvas = canvas
        self.targetCoordinate = (coordinate[1], coordinate[0])

    def interactive(self) -> Callable[[None], None] | None:
        return self.interactiveFunction

    def getObjectType(self) -> str:
        return self.objectType

    def isInteractive(self) -> bool:
        return self.interactiveFunction != None

class img(LevelObject):
    __counter: int = -1
    __PhotoImg: List[ImageTk.PhotoImage] = []
    def __init__(self, imgPath: str, size: Tuple[int, int], interactive: Callable[[None], None] | None = None):
        self.objectType = "IMAGE"
        self.interactive = interactive
        self.object: Image = Image.open(imgPath)
        self.object.thumbnail(size)

    def addToCanvas(self, canvas: Canvas, coordinate: Tuple[int, int]) -> Any:
        super().addToCanvas(canvas, coordinate)
        self.__PhotoImg.append(ImageTk.PhotoImage(self.object))
        self.__counter += 1
        return canvas.create_image(self.targetCoordinate, anchor=NW, image=self.__PhotoImg[self.__counter])
