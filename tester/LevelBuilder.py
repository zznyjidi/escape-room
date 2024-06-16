from module.LevelBuilder import LevelBuilder
from module.PlayerController import PlayerController
from module.MovableObject import Player
from module.TileLoader import TileLoader
import levels.testLevel
import ttkbootstrap as ttk

window = ttk.Window()

Controller = PlayerController(window, debug=True)

level = LevelBuilder(window, debug=True)
level.loadLevel(levels.testLevel.LEVEL)
level.buildLevel()

player = Player(level, TileLoader("assets/player_tile_32.png", tileSize=(32, 48), blankHeight=16, emptyFirstRow=True), (2, 1), debug=True)
Controller.attachPlayer(player)

level.pack(fill="both", expand=True)

#window.after(1000, lambda: level.toImage().show())

window.mainloop()
