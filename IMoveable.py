from abc import ABC, abstractmethod
from pygame import Vector2


class IMoveable(ABC):
    pos: Vector2 = Vector2(0, 0)

    @abstractmethod
    def move(self):
        pass
