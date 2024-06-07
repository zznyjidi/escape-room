from typing import Final, List, Dict

MOVE_UP:    Final[str] = 'w'
MOVE_DOWN:  Final[str] = 's'
MOVE_LEFT:  Final[str] = 'a'
MOVE_RIGHT: Final[str] = 'd'

INTERACTIVE_SELECT: Final[str] = 'f'
INTERACTIVE_CANCEL: Final[str] = 'x'

ListNameList: Final[List[str]] = ["MOVE", "INTERACTIVE", "OTHER"]
def keyToListMapper(key: str) -> str:
    if key in [MOVE_UP, MOVE_DOWN, MOVE_LEFT, MOVE_RIGHT]:
        return "MOVE"
    if key in [INTERACTIVE_SELECT, INTERACTIVE_CANCEL]:
        return "INTERACTIVE"
    else:
        return "OTHER"

keymap: Final[Dict[str, str]] = {
    "MOVE_UP": MOVE_UP,
    "MOVE_DOWN": MOVE_DOWN,
    "MOVE_LEFT": MOVE_LEFT,
    "MOVE_RIGHT": MOVE_RIGHT,
    "INTERACTIVE_SELECT": INTERACTIVE_SELECT,
    "INTERACTIVE_CANCEL": INTERACTIVE_CANCEL,
}
