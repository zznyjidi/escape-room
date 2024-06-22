from module.LevelDescriber import LevelDescriber
from module.LevelObject import img, interact
from module.LevelManager import LevelManager
from module.LevelBuilder import PlaceHolder as PH
from PIL import Image, ImageTk
import ttkbootstrap as ttk
import tkinter.messagebox
import config.drawing

LevelPassword = "PASSWORD"
gridBlockSize = config.drawing.gridBlockSize
LEVEL = LevelDescriber(NextLevelPos=(2, 4))

def computerInteract():
    window = ttk.Window("Computer", "darkly")
    window.geometry("500x300")
    window.resizable(False, False)
    LevelMaster: LevelManager = LEVEL.MASTER
    LevelMaster.playerController.inputDisable()
    
    doorControllerFrame = ttk.Frame(window)
    doorControllerFrame.pack(fill="none", expand=True)
    doorControllerLabel = ttk.Label(doorControllerFrame, text="Wireless Door Controller v1.0")
    doorControllerLabel.pack(padx=5, pady=5)
    doorStatusLabel = ttk.Label(doorControllerFrame)
    doorStatusLabel.pack(pady=5)
    def updateStatus():
        if LEVEL.UNLOCKED:
            doorStatusLabel.configure(text="Door is Unlocked", bootstyle=ttk.SUCCESS)
        else:
            doorStatusLabel.configure(text="Door is Locked", bootstyle=ttk.DANGER)
    def lockDoor():
        LEVEL.lock()
        updateStatus()
    def unlockDoor():
        LEVEL.unlock()
        updateStatus()
    updateStatus()
    lockButton = ttk.Button(doorControllerFrame, text="Lock", state="disabled", command=lockDoor)
    lockButton.pack()
    unlockButton = ttk.Button(doorControllerFrame, text="Unlock", state="disabled", command=unlockDoor)
    unlockButton.pack(pady=5)
    
    loginFrame = ttk.Frame(window)
    loginFrame.place(relx=0.5, rely=0.5, anchor="center")
    passwordLabel = ttk.Label(loginFrame, text="Password", font=("Consolas", 8))
    passwordLabel.pack(pady=5)
    passwordEntry = ttk.Entry(loginFrame, width=8, show="*", font=("Consolas", 18))
    passwordEntry.pack(padx=5)
    def checkPassword():
        password = passwordEntry.get()
        if password == LevelPassword:
            loginFrame.place_forget()
            lockButton.configure(state="normal")
            unlockButton.configure(state="normal")
    loginButton = ttk.Button(loginFrame, text="LOGIN", command=checkPassword)
    loginButton.pack(pady=5)
    
    window.mainloop()
    LevelMaster.playerController.inputEnable()

computer = img(
    "assets/level1/computer.png", 
    (gridBlockSize * 0.9, gridBlockSize * 0.9), 
    computerInteract
)

def whiteboardInteract():
    global LV1_whiteboardImgTk
    window = ttk.Window("Whiteboard")
    window.resizable(False, False)
    LevelMaster: LevelManager = LEVEL.MASTER
    LevelMaster.playerController.inputDisable()
    
    whiteboardImg = Image.open("assets/level1/whiteboard_content.png")
    LV1_whiteboardImgTk = ImageTk.PhotoImage(whiteboardImg, master=window)
    whiteboardContent = ttk.Label(window, image=LV1_whiteboardImgTk)
    whiteboardContent.pack(fill="both", expand=True)
    
    window.mainloop()
    LevelMaster.playerController.inputEnable()

whiteboard = img(
    "assets/level1/whiteboard.png", 
    (int(gridBlockSize * 0.2), int(gridBlockSize * 2.8)), 
    whiteboardInteract, 
    useResize=True, 
    offset=(-gridBlockSize * 0.5, 0)
)
whiteboardBlock = interact(
    whiteboardInteract, 
    collision=True
)

door = img(
    "assets/level1/door.png", 
    (gridBlockSize * 0.9, gridBlockSize * 0.9), 
    None
)

DESCRIBER = [
    [None, computer, None],
    [None, PH.SPAWN, None], 
    [None, None,     None],
]

LEVEL.setDescriber(DESCRIBER, nextLevelImg=door)

LEVEL.GRID.addItem(1, 4, whiteboardBlock, overwrite=True)
LEVEL.GRID.addItem(2, 4, whiteboard, overwrite=True)
LEVEL.GRID.addItem(3, 4, whiteboardBlock, overwrite=True)

def doorLockedPopup():
    tkinter.messagebox.showwarning("DOOR", "The Door is Locked! ")

LEVEL.setLockedFunction(doorLockedPopup)
