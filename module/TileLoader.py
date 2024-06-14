from typing import Tuple
import warnings
import PIL.Image

class TileLoader:
    def __init__(self, imgFile: str, *, tileSize: Tuple[int, int] = (32, 64), blankHeight: int = 0, emptyFirstRow: bool = False):
        """
        #### Load Tile from Image. 

        Args:
            imgFile (str): Image that Contains all the Tiles. 
            tileSize (Tuple[int, int], optional): The Size of each Tile. Defaults to (32, 64).
            blankHeight (int, optional): Empty Height between each Tile. . Defaults to 0.
            emptyFirstRow (bool, optional): Have a Empty Line before all Tiles. Defaults to False.
        """
        self.tile = PIL.Image.open(imgFile)
        self.tileSize = tileSize
        self.blankHeight = blankHeight
        self.emptyFirstLine = emptyFirstRow

    def getTile(self, row: int, col: int) -> PIL.Image:
        xStart = (self.tileSize[0] * col)
        yStart = (self.tileSize[1] * row) + (self.blankHeight * (row + (1 if self.emptyFirstLine else 0)))
        xEnd = xStart + self.tileSize[0]
        yEnd = yStart + self.tileSize[1]
        
        if (xStart < 0) or (yStart < 0) or (xEnd > self.tile.width) or (yEnd > self.tile.height):
            warnings.warn("Trying to Load a Map out of the Image. Returning Empty Image. ")
            return PIL.Image.new("RGBA", self.tileSize)
        
        return self.tile.crop((xStart, yStart, xEnd, yEnd))
