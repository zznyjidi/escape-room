from typing import Dict, Tuple

gridBlockSize: int = 100

tileConfig: Dict[str, Tuple[int, int]] = {
    "STAND_FRONT": (0, 4),
    "STAND_BACK":  (0, 2),
    "STAND_LEFT":  (0, 3),
    "STAND_RIGHT": (0, 1),

    "WALK_FRONT_START": (9, 36),
    "WALK_FRONT_STOP":  (9, 47),
    "WALK_BACK_START":  (9, 12),
    "WALK_BACK_STOP":   (9, 23),
    "WALK_LEFT_START":  (9, 24),
    "WALK_LEFT_STOP":   (9, 35),
    "WALK_RIGHT_START": (9, 0),
    "WALK_RIGHT_STOP":  (9, 11),
}
