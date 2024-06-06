from module.App import App
from module.PlayerController import PlayerController
from test.ExampleMoveableObject import MoveableObject

appMain = App()
appController = PlayerController(appMain, debug=True)
testObject = MoveableObject()
appController.attachPlayer(testObject)
appMain.startApp()
