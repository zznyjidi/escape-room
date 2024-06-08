import time, threading
from typing import Callable

class timerDisplay:
    def __init__(self):
        """
        #### Template Timer Display
        """
        self.hour: int = 0
        self.mins: int = 0
        self.secs: int = 0

    def update(self, timeSec: int):
        """
        #### Update Timer

        Args:
            timeSec (int): Time Left in Second. 
        """
        self.mins, self.secs = divmod(timeSec, 60)
        self.hour, self.mins = divmod(self.mins, 60)

class timer:
    updateObjects = []

    def __init__(self, startTime: int, timerEndAction: Callable[[None], None], debug: bool = False):
        """
        #### Create a new Timer

        Args:
            startTime (int): Time to start with. 
            timerEndAction (Callable[[None], None]): Function to Call when timer is end. 
            debug (bool, optional): Run in debug Mode. Defaults to False.
        """
        self.__debug = debug
        self.timeSec = startTime
        self.timerEndAction = timerEndAction
        self.timerThread = threading.Thread(target=self.timerUpdater, daemon=True)

    def timerUpdater(self):
        """
        #### Timer Updating Thread
        Use with `self.timerThread = threading.Thread(target=self.timerUpdater, daemon=True)`
        """
        while self.timeSec:
            for i in self.updateObjects:
                i.update(self.timeSec)
            time.sleep(1)
            self.timeSec -= 1

    def startTimer(self):
        """
        #### Start timer update thread. 
        """
        self.timerThread.start()

    def attachObject(self, object: timerDisplay):
        """
        #### Attach a new timerDisplay Object. 

        Args:
            object (timerDisplay): timerDisplay that display the left time. 
        """
        self.updateObjects.append(object)

    def detachObject(self, object: timerDisplay):
        """
        #### Detach a attached timerDisplay Object. 

        Args:
            object (timerDisplay): timerDisplay to be detach. 
        """
        try:
            self.updateObjects.remove(object)
        except ValueError:
            self.debugPrint(f"Trying to detach a Non-attached Object: {object}")

    def debugPrint(self, message):
        """
        #### Print if in Debug Mode. 

        Args:
            message: Message to Print. 
        """
        print(f"[{time.asctime()}][PlayerController] {message}") if self.__debug else None
