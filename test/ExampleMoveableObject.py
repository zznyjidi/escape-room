import time

class MoveableObject:
    def __init__(self):
        pass
    def isMoveable(self):
        return True
    def move(self, moveInfo):
        print(f"[{time.asctime()}][ExampleMoveableObject] {moveInfo}")
