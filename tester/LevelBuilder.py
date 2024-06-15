from module.LevelBuilder import LevelBuilder
from module.VirtualGrid import VirtualGrid
from module.PlayerController import PlayerController
from module.MovableObject import Player
from module.TileLoader import TileLoader
import levels.testLevel
import config.drawing
import ttkbootstrap as ttk

window = ttk.Window()

Controller = PlayerController(window, True)

levelGrid = VirtualGrid(3, 4, debug=True)
levelGrid.importGrid(levels.testLevel.describer)

level = LevelBuilder(window, True)
level.loadLevel(levelGrid)
level.buildLevel()

player = Player(level.canvas, TileLoader("assets/player_tile_32.png", tileSize=(32, 48), blankHeight=16, emptyFirstRow=True), (config.drawing.gridBlockSize/2, config.drawing.gridBlockSize/2))
Controller.attachPlayer(player)

level.pack()

#window.after(1000, lambda: level.toImage().show())

window.mainloop()
