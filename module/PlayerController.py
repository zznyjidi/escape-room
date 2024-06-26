from typing import Callable, Dict, List, Tuple, Final
from module.MovableObject import MoveableObject
import ttkbootstrap as ttk
import threading, time
import config.keymap

class PlayerController:
    __PressedKey: Dict[str, list] = {}
    __updateReady: bool = True
    __updateLocked: bool = False

    def __init__(self, window: ttk.Window, debug: bool = False):
        """
        #### Listen to Tkinter Key Presses and Control a Moveable Object that is attached. 

        To Attach a Object, Run `attachPlayer(Object)`  
        To Detach the Object, Run `detachPlayer(Object)`  
        To Set a Custom Keymap, Run `setKeymap(keyMap, listMap)`, see `config.keymap` for reference.  

        Args:
            window (ttk.Window): Master Window that the PlayerController will listen the key presses. 
            debug (bool, optional): Run in debug Mode. Defaults to False.
        """
        self.__debug: bool = debug
        self.__window: ttk.Window = window
        self.setKeymap()
        self.detachPlayer()
        self.__window.bind("<KeyPress>", self.__keyPressedHook)
        self.__window.bind("<KeyRelease>", self.__keyReleaseHook)
        self.__OperationThread: threading.Thread =  threading.Thread(target=self.__ControllerOperationThread, daemon=True)
        self.CurrentPressedKeys = {}
        self.__OperationThread.start()


    def setKeymap(self, keymap: Dict[str, str] = config.keymap.keymap, keyToListMapper: Callable[[str], str] = config.keymap.keyToListMapper):
        """
        #### Set Keymap For Player Controller

        Args:
            keymap (Dict[str], optional): Key Map Dictionary. Defaults to config.keymap.keymap.
            keyToListMapper (Callable[[str], str], optional): Key to KeyGroup List Mapper. Defaults to config.keymap.keyToListMapper.
        """
        self.__keymap: Dict[str, str] = keymap
        self.__keyToListMapper: Callable[[str], str] = keyToListMapper
        for i in config.keymap.ListNameList:
            self.__PressedKey[i] = []


    def havePressedKey(self) -> bool:
        """
        #### True if Have Any Key Pressed. 

        Returns:
            bool: Have Any Key Pressed. 
        """
        keyPressed: int = sum(map(len, self.__PressedKey.values()))
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
            PressedKeys: List[str] = list(map(lambda x: x[0], i))
            if key in PressedKeys:
                return True
        return False


    def attachPlayer(self, PlayerObject: MoveableObject):
        """
        #### Attach Player Controller to a Controllable Object. 

        Args:
            PlayerObject (MoveableObject): Object to be Attached. 
        """
        self.__playerObject = PlayerObject
        self.debugPrint(f"Player Object Attached: {PlayerObject}")


    def detachPlayer(self):
        """
        #### Detach Player Object from Player Controller. 
        """
        self.__playerObject: MoveableObject | None = None
        self.debugPrint(f"Player Object Detached. ")


    def inputEnable(self, clearQuery: bool = True):
        """
        #### Enable Input for PlayerController

        Args:
            clearQuery (bool, optional): Clear Unhandled Pressed Key Query. Defaults to True.
        """
        if clearQuery:
            self.clearQuery()
        self.__updateLocked = False


    def inputDisable(self, clearQuery: bool = True):
        """
        #### Disable Input for PlayerController

        Args:
            clearQuery (bool, optional): Clear Unhandled Pressed Key Query. Defaults to True.
        """
        self.__updateLocked = True
        if clearQuery:
            self.clearQuery()


    def clearQuery(self):
        """
        #### Clear Unhandled Pressed Key Query. 
        """
        for i in self.__PressedKey.values():
            i.clear()


    def __keyPressedHook(self, event):
        """
        #### Handle Tkinter Key Pressed Event. 
        Use with `self.__window.bind("<KeyPress>", self.__keyPressedHook)`

        Args:
            event: Event From Tkinter. 
        """
        key: str = event.keysym
        targetList: str = self.__keyToListMapper(key)
        self.debugPrint(f"Key Pressed: {targetList}: {key}")

        self.__PressedKey[targetList].append((key, 1, int(time.time())))


    def __keyReleaseHook(self, event):
        """
        #### Handle Tkinter Key Release Event. 
        Use with `self.__window.bind("<KeyRelease>", self.__keyReleaseHook)`

        Args:
            event: Event From Tkinter. 
        """
        key: str = event.keysym
        targetList: str = self.__keyToListMapper(key)
        self.debugPrint(f"Key Release: {targetList}: {key}")

        self.__PressedKey[targetList].append((key, 0, int(time.time())))


    def __keyToAngle(self, PressedKeys: List[str]) -> List[str]:
        """
        #### Translate Pressed Key to Direction Base on Key Map. 

        Args:
            PressedKeys (List[str]): Keys being Pressed. 

        Returns:
            List[str]: Directions: LEFT, RIGHT, UP, and/or DOWN. 
        """
        MoveAngle: List[str] = []
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
            if not self.__updateLocked:
                pass
            if not self.havePressedKey():
                pass

            PressedKeys = {}
            for keyList, keys in self.__PressedKey.items():
                PressedKeys[keyList] = keys[:]
                keys.clear()

            if not self.__playerObject is None:
                if len(PressedKeys["MOVE"]):
                    actions = []
                    self.CurrentPressedKeys["MOVE"] = []
                    for keyPress in PressedKeys["MOVE"]:
                        if keyPress[1]:
                            self.CurrentPressedKeys["MOVE"].append(keyPress[0]) if not keyPress[0] in self.CurrentPressedKeys["MOVE"] else None
                        else:
                            self.CurrentPressedKeys["MOVE"].remove(keyPress[0]) if keyPress[0] in self.CurrentPressedKeys["MOVE"] else None
                        if len(self.CurrentPressedKeys["MOVE"]):
                            actions.append(self.CurrentPressedKeys["MOVE"][:])
                    for action in actions:
                        self.__playerObject.move(self.__keyToAngle(action))
                if len(PressedKeys["INTERACTIVE"]):
                    actions = list(map(lambda keyPress: keyPress[0] if keyPress[1] else None, PressedKeys["INTERACTIVE"]))
                    while None in actions:
                        actions.remove(None)
                    if config.keymap.keymap["INTERACTIVE_SELECT"] in actions:
                        self.__playerObject.interact()

    def debugPrint(self, message):
        """
        #### Print if in Debug Mode. 

        Args:
            message: Message to Print. 
        """
        print(f"[{time.asctime()}][PlayerController] {message}") if self.__debug else None
