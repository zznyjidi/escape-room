from module.LevelManager import LevelManager
from module.TileLoader import TileLoader
import levels.testLevel
import ttkbootstrap as ttk

window = ttk.Window()

game = LevelManager(debug=True)

game.addLevel(levels.testLevel.LEVEL, levels.testLevel.LEVEL_LOCKED)
game.addPlayerTiles(TileLoader("assets/player_tile_32.png", tileSize=(32, 48), blankHeight=16, emptyFirstRow=True))
game.initGame(window)

#window.after(1000, lambda: level.toImage().show())

window.mainloop()
