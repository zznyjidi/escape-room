from module.GlobalTimer import timerDisplay
import ttkbootstrap as ttk

class GUITimerDisplay(timerDisplay):
    def __init__(self, master):
        super().__init__()
        self.TimerLabel = ttk.Label(master)

    def update(self, timeSec: int):
        super().update(timeSec)
        self.TimerLabel.config(text="{}:{:02d}:{:02d}".format(self.hour, self.mins, self.secs))
