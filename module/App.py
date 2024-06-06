import ttkbootstrap as ttk

class App(ttk.Window):
    def __init__(self, theme: str = "darkly", debug: bool = False):
        super().__init__(themename=theme)
    def startApp(self):
        self.mainloop()
