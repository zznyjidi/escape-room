from typing import Dict, Tuple

gridBlockSize: int = 64

tileConfig: Dict[str, Tuple[int, int]] = {
    "STAND_DOWN":  (0, 3),
    "STAND_UP":    (0, 1),
    "STAND_LEFT":  (0, 2),
    "STAND_RIGHT": (0, 0),

    "WALK_DOWN_START":  (16, 12),
    "WALK_DOWN_STOP":   (16, 15),
    "WALK_UP_START":    (16, 4),
    "WALK_UP_STOP":     (16, 7),
    "WALK_LEFT_START":  (16, 8),
    "WALK_LEFT_STOP":   (16, 11),
    "WALK_RIGHT_START": (16, 0),
    "WALK_RIGHT_STOP":  (16, 3),
}
