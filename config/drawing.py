from typing import Dict, Tuple

gridBlockSize: int = 64

tileConfig: Dict[str, Tuple[int, int]] = {
    "STAND_DOWN":  (0, 4),
    "STAND_UP":    (0, 2),
    "STAND_LEFT":  (0, 3),
    "STAND_RIGHT": (0, 1),

    "WALK_DOWN_START":  (9, 36),
    "WALK_DOWN_STOP":   (9, 47),
    "WALK_UP_START":    (9, 12),
    "WALK_UP_STOP":     (9, 23),
    "WALK_LEFT_START":  (9, 24),
    "WALK_LEFT_STOP":   (9, 35),
    "WALK_RIGHT_START": (9, 0),
    "WALK_RIGHT_STOP":  (9, 11),
}
