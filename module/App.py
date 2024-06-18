import ttkbootstrap as ttk
from module.LevelManager import LevelManager
from module.TileLoader import TileLoader
import levels.Level1

class App(ttk.Window):
    def __init__(self, theme: str = "darkly", debug: bool = False):
        self.__debug = debug
        super().__init__(themename=theme)
        
        game = LevelManager(debug=debug)

        game.addLevel(levels.Level1.LEVEL)
        game.addPlayerTiles(TileLoader("assets/player_tile_32.png", tileSize=(32, 48), blankHeight=16, emptyFirstRow=True))
        game.initGame(self)

    def startApp(self):
        self.mainloop()
