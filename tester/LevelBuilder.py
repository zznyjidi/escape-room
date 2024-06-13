from module.LevelBuilder import LevelBuilder
from module.VirtualGrid import VirtualGrid
import levels.testLevel
import ttkbootstrap as ttk

window = ttk.Window()

levelGrid = VirtualGrid(3, 3, 100, True)
levelGrid.importGrid(levels.testLevel.describer)

level = LevelBuilder(window)
level.loadLevel(levelGrid)
level.buildLevel()

level.pack()

window.mainloop()
