from module.App import App
import sys

try:
    debug: bool = True if "--debug" in sys.argv else False
    theme: str = (sys.argv[sys.argv.index("--theme")+1]) if ("--theme" in sys.argv) else "darkly"
except IndexError as e:
    print(f"Invalid Args: {e}")
    exit()

appMain = App(theme=theme, debug=debug)
appMain.startApp()
