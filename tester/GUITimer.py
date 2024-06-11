from module.GlobalTimer import timer
from module.GUITimerDisplay import GUITimerDisplay
import ttkbootstrap as ttk

window = ttk.Window()

GTimer = timer(10, lambda: None, True)
GTimerDisplay = GUITimerDisplay(window)
GTimerDisplay.TimerLabel.pack()

GTimer.attachObject(GTimerDisplay)
GTimer.start()

window.mainloop()
