from typing import Callable, Dict, List
import ttkbootstrap as ttk
import threading, time
import config.keymap

class PlayerController:
    __PressedKey = {}
    __updateReady = False
    __haveUpdate = False

    def __init__(self, window: ttk.Window, debug: bool = False):
        """
        #### Listen to Tkinter Key Presses and Control a Moveable Object that is attached. 

        To Attach a Object, Run `attachPlayer(Object)`
        To Detach the Object, Run `detachPlayer(Object)`
        To Set a Custom Keymap, Run `setKeymap(keyMap, listMap)`, see `config.keymap` for reference. 

        Args:
            window (ttk.Window): _description_
            debug (bool, optional): _description_. Defaults to False.
        """
        self.__debug = debug
        self.__window = window
        self.setKeymap()
        self.__window.bind("<KeyPress>", self.__keyPressedHook)
        self.__window.bind("<KeyRelease>", self.__keyReleaseHook)
        self.__OperationThread =  threading.Thread(target=self.__ControllerOperationThread, daemon=True)
        self.__OperationThread.start()


    def setKeymap(self, keymap: Dict[str] = config.keymap.keymap, keyToListMapper: Callable[[str], str] = config.keymap.keyToListMapper):
        """
        #### Set Keymap For Player Controller

        Args:
            keymap (Dict[str], optional): Key Map Dictionary. Defaults to config.keymap.keymap.
            keyToListMapper (Callable[[str], str], optional): Key to KeyGroup List Mapper. Defaults to config.keymap.keyToListMapper.
        """
        self.__keymap = keymap
        self.__keyToListMapper = keyToListMapper


    def havePressedKey(self) -> bool:
        """
        #### True if Have Any Key Pressed. 

        Returns:
            bool: Have Any Key Pressed. 
        """
        keyPressed = sum(map(len, self.__PressedKey.values()))
        return bool(keyPressed)


    def isPressed(self, key: str) -> bool:
        """
        #### Check If the Key is Presses

        Args:
            key (str): Key to Check. 

        Returns:
            bool: Key is Pressed. 
        """
        for i in self.__PressedKey.values():
            if key in i:
                return True
        return False


    def attachPlayer(self, PlayerObject):
        """
        #### Attach Player Controller to a Controllable Object. 

        Args:
            PlayerObject (_type_): Object to be Attached. 
        """
        self.__playerObject = PlayerObject
        self.debugPrint(f"Player Object Attached: {PlayerObject}")


    def detachPlayer(self):
        """
        #### Detach Player Object from Player Controller. 
        """
        self.__playerObject = None
        self.debugPrint(f"Player Object Detached. ")


    def __keyPressedHook(self, event):
        """
        #### Handle Tkinter Key Pressed Event. 
        Use with `self.__window.bind("<KeyPress>", self.__keyPressedHook)`

        Args:
            event: Event From Tkinter. 
        """
        while not self.__updateReady:
            pass
        key = event.keysym
        targetList = self.__keyToListMapper(key)

        self.debugPrint(f"Key Pressed: {targetList}: {key}")

        if self.isPressed(key):
            return

        self.__PressedKey[targetList].append(key)
        self.__haveUpdate = True


    def __keyReleaseHook(self, event):
        """
        #### Handle Tkinter Key Release Event. 
        Use with `self.__window.bind("<KeyRelease>", self.__keyReleaseHook)`

        Args:
            event: Event From Tkinter. 
        """
        while not self.__updateReady:
            pass
        key = event.keysym
        targetList = self.__keyToListMapper(key)

        self.debugPrint(f"Key Release: {targetList}: {key}")

        if not self.isPressed(key):
            return

        self.__PressedKey[targetList].remove(key)
        self.__haveUpdate = True


    def __keyToAngle(self) -> List[str]:
        """
        #### Translate Current Pressed Key to Direction Base on Key Map. 

        Returns:
            List[str]: Directions: LEFT, RIGHT, UP, and/or DOWN. 
        """
        PressedKeys = self.__PressedKey["MOVE_KEY"]
        MoveAngle = []
        if self.__keymap["MOVE_LEFT"] in PressedKeys:
            MoveAngle.append("LEFT")
        if self.__keymap["MOVE_RIGHT"] in PressedKeys:
            if "LEFT" in MoveAngle:
                MoveAngle.remove("LEFT")
            else:
                MoveAngle.append("RIGHT")
        if self.__keymap["MOVE_UP"] in PressedKeys:
            MoveAngle.append("UP")
        if self.__keymap["MOVE_DOWN"] in PressedKeys:
            if "UP" in MoveAngle:
                MoveAngle.remove("UP")
            else:
                MoveAngle.append("DOWN")
        return MoveAngle


    def __ControllerOperationThread(self):
        """
        #### Thread that Handle Key Press to Object Movements. 
        """
        while True:
            while not self.__haveUpdate:
                pass
            self.__updateReady = False
            if self.__playerObject == None:
                pass
            if not self.havePressedKey():
                pass
            if not self.__playerObject.ismMoveable:
                pass
            if len(self.__PressedKey["MOVE_KEY"]):
                self.__playerObject.move(self.__keyToAngle())
            self.__haveUpdate = False
            self.__updateReady = True


    def debugPrint(self, message):
        """
        #### Print if in Debug Mode. 

        Args:
            message: Message to Print. 
        """
        print(f"[{time.asctime()}]{message}") if self.__debug else None
