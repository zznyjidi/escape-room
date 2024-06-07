import ttkbootstrap as ttk
from module.PlayerController import PlayerController

class App(ttk.Window):
    def __init__(self, theme: str = "darkly", debug: bool = False):
        self.__debug = debug
        super().__init__(themename=theme)
        self.__playerController: PlayerController = PlayerController(self, debug=debug)


    def startApp(self):
        self.mainloop()
