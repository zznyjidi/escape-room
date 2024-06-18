from PIL import Image, ImageTk
from ttkbootstrap import Canvas, CENTER
from typing import Tuple, List, Any, Callable

class LevelObject:
    objectType: str = "BASE"
    targetCanvas: Canvas
    targetCoordinate: Tuple[int, int]
    collision = True

    def addToCanvas(self, canvas: Canvas, coordinate: Tuple[int, int]):
        """
        #### Add Object to Canvas. 

        Args:
            canvas (Canvas): Target Canvas. 
            coordinate (Tuple[int, int]): Coordinate on Canvas. 
        """
        self.targetCanvas = canvas
        self.targetCoordinate = (coordinate[1], coordinate[0])

    def interactive(self) -> Callable[[None], None] | None:
        """
        #### Interact with the Object. 

        Returns:
            Callable[[None], None] | None: Function to Call to Interact. 
        """
        return self.interactiveFunction

    def getObjectType(self) -> str:
        """
        #### Get the Type of the Object. 

        Returns:
            str: Object Type. 
        """
        return self.objectType

    def isInteractive(self) -> bool:
        """
        #### Check if it have a feature to interact with. 

        Returns:
            bool: Is Interactive. 
        """
        return not self.interactiveFunction is None

class img(LevelObject):
    __PhotoImg: List[ImageTk.PhotoImage] = []
    def __init__(self, imgPath: str, size: Tuple[int, int], interactive: Callable[[None], None] | None = None, collision: bool = True):
        """
        #### Create a new Image in Level. 

        Args:
            imgPath (str): Path of the Image File .
            size (Tuple[int, int]): Target Size of the Image. 
            interactive (Callable[[None], None] | None, optional): Function to Run when interact with. Defaults to None.
            collision (bool, optional): Have a Hitbox. Defaults to True.
        """
        self.objectType = "IMAGE"
        self.interactiveFunction = interactive
        self.collision = collision
        self.object: Image = Image.open(imgPath)
        self.object.thumbnail(size)

    def addToCanvas(self, canvas: Canvas, coordinate: Tuple[int, int]) -> Any:
        """
        #### Add Image to the Canvas. 

        Args:
            canvas (Canvas): Target Canvas. 
            coordinate (Tuple[int, int]): Coordinate on Canvas. 

        Returns:
            Any: Image Reference for Tkinter. 
        """
        super().addToCanvas(canvas, coordinate)
        self.__PhotoImg.append(ImageTk.PhotoImage(self.object))
        return canvas.create_image(self.targetCoordinate, anchor=CENTER, image=self.__PhotoImg[-1])

class interact(LevelObject):
    def __init__(self, interactive: Callable[[None], None], collision: bool = False):
        self.objectType = "INTERACT"
        self.interactiveFunction = interactive
        self.collision = collision
