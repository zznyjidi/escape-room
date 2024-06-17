from typing import Dict, Tuple

gridBlockSize: int = 64

tileConfig: Dict[str, Tuple[int, int]] = {
    "STAND_DOWN":  (0, 3),
    "STAND_UP":    (0, 1),
    "STAND_LEFT":  (0, 2),
    "STAND_RIGHT": (0, 0),

    "WALK_DOWN_START":  (2, 18),
    "WALK_DOWN_STOP":   (2, 23),
    "WALK_UP_START":    (2, 6),
    "WALK_UP_STOP":     (2, 11),
    "WALK_LEFT_START":  (2, 12),
    "WALK_LEFT_STOP":   (2, 17),
    "WALK_RIGHT_START": (2, 0),
    "WALK_RIGHT_STOP":  (2, 5),
}
