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
        #### Update Timer. 

        Args:
            timeSec (int): Time Left in Second. 
        """
        self.timeSec = timeSec
        self.mins, self.secs = divmod(self.timeSec, 60)
        self.hour, self.mins = divmod(self.mins, 60)

class timer:
    __updateObjects = []
    __paused = False
    __stopped = False

    def __init__(self, startTime: int, timerEndAction: Callable[[None], None], debug: bool = False):
        """
        #### Create a new Timer

        Args:
            startTime (int): Time to start with. 
            timerEndAction (Callable[[None], None]): Function to Call when timer is end. 
            debug (bool, optional): Run in debug Mode. Defaults to False.
        """
        self.__debug = debug
        self.__timeSec = startTime
        self.__timerEndAction = timerEndAction
        self.__timerThread = threading.Thread(target=self.timerUpdater, daemon=True)
        self.debugPrint(f"Timer Created, Time: {startTime} sec, Timer End Action: {timerEndAction}. ")

    def timerUpdater(self):
        """
        #### Timer Updating Thread
        Use with `self.__timerThread = threading.Thread(target=self.timerUpdater, daemon=True)`
        """
        while (self.__timeSec >= 0) and (not self.__stopped):
            while self.__paused:
                pass
            for i in self.__updateObjects:
                i.update(self.__timeSec)
            time.sleep(1)
            self.__timeSec -= 1
        self.debugPrint("Timer Ended. ")
        if not self.__stopped:
            self.__timerEndAction()
            self.debugPrint(f"Timer End Action Triggered: {self.__timerEndAction}")

    def setTime(self, timeSec: int):
        """
        #### Set Timer Time Left. 

        Args:
            timeSec (int): New Timer Countdown Time. 
        """
        self.__timeSec = timeSec
        self.debugPrint(f"New Time Set: {timeSec}")

    def start(self):
        """
        #### Start timer update thread. 
        """
        self.__stopped = False
        self.__timerThread.start()
        self.debugPrint("Timer Started. ")

    def pause(self):
        """
        #### Pause the timer. 
        """
        self.__paused = True
        self.debugPrint("Timer Paused. ")

    def resume(self):
        """
        #### Resume the timer. 
        """
        self.__paused = False
        self.debugPrint("Timer Resumed. ")

    def stop(self):
        """
        #### Stop the timer. 
        """
        self.__stopped = True
        self.debugPrint("Timer Stopped by Function Call. ")

    def attachObject(self, object: timerDisplay):
        """
        #### Attach a new timerDisplay Object. 

        Args:
            object (timerDisplay): timerDisplay that display the left time. 
        """
        self.__updateObjects.append(object)
        self.debugPrint(f"Object Attached: {object}")

    def detachObject(self, object: timerDisplay):
        """
        #### Detach a attached timerDisplay Object. 

        Args:
            object (timerDisplay): timerDisplay to be detach. 
        """
        try:
            self.__updateObjects.remove(object)
            self.debugPrint(f"Object Detached: {object}")
        except ValueError:
            self.debugPrint(f"Trying to detach a Non-attached Object: {object}")

    def debugPrint(self, message):
        """
        #### Print if in Debug Mode. 

        Args:
            message: Message to Print. 
        """
        print(f"[{time.asctime()}][GlobalTimer] {message}") if self.__debug else None
