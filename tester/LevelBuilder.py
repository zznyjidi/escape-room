from module.LevelBuilder import LevelBuilder
from module.VirtualGrid import VirtualGrid
import levels.testLevel
import ttkbootstrap as ttk

window = ttk.Window()

levelGrid = VirtualGrid(3, 4, 100, True)
levelGrid.importGrid(levels.testLevel.describer)

level = LevelBuilder(window, True)
level.loadLevel(levelGrid)

level.pack()

window.after(500, level.buildLevel)
#window.after(5000, lambda: level.toImage().show())

window.mainloop()
