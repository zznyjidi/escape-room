
MOVE_UP = 'w'
MOVE_DOWN = 's'
MOVE_LEFT = 'a'
MOVE_RIGHT = 'd'

INTERACTIVE_SELECT = 'f'
INTERACTIVE_CANCEL = 'x'

ListNameList = ["MOVE", "INTERACTIVE", "OTHER"]
def keyToListMapper(key: str) -> str:
    if key in [MOVE_UP, MOVE_DOWN, MOVE_LEFT, MOVE_RIGHT]:
        return "MOVE"
    if key in [INTERACTIVE_SELECT, INTERACTIVE_CANCEL]:
        return "INTERACTIVE"
    else:
        return "OTHER"

keymap = {
    "MOVE_UP": MOVE_UP,
    "MOVE_DOWN": MOVE_DOWN,
    "MOVE_LEFT": MOVE_LEFT,
    "MOVE_RIGHT": MOVE_RIGHT,
    "INTERACTIVE_SELECT": INTERACTIVE_SELECT,
    "INTERACTIVE_CANCEL": INTERACTIVE_CANCEL,
}
