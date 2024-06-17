from module.GlobalTimer import timerDisplay
import ttkbootstrap as ttk
from tkinter import TclError

class GUITimerDisplay(timerDisplay):
    def __init__(self, *args, **kwargs):
        """
        #### GUI Timer Display Label. 
        Display time left when attached to a timer. 
        Args will be pass into Label Creation. 
        """
        super().__init__()
        self.TimerLabel: ttk.Label = ttk.Label(*args, **kwargs)

    def update(self, timeSec: int):
        """
        #### Update the Timer Display Label. 

        Args:
            timeSec (int): Time Left in Second. 
        """
        super().update(timeSec)
        try:
            self.TimerLabel.config(text="{}:{:02d}:{:02d}".format(self.hour, self.mins, self.secs))
        except TclError as Error:
            raise self.DisplayOutdatedError(f"Tkinter Object No longer Exist: {Error}")

    def pack(self, *args, **kwargs):
        """
        #### Pack the Label. 
        Args will be pass into Label.pack. 
        """
        self.TimerLabel.pack(*args, **kwargs)

    def pack_forget(self):
        """
        #### Pack Forget the Label. 
        """
        self.TimerLabel.pack_forget()

    def place(self, *args, **kwargs):
        """
        #### Place the Label. 
        """
        self.TimerLabel.place(*args, **kwargs)

    def place_forget(self):
        """
        #### Place Forget the Label. 
        """
        self.TimerLabel.place_forget()
