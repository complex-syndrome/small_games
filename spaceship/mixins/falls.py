from abc import ABC

from utils.vectors import Vec2


class Falls(ABC):
    def __init__(self, pos: Vec2) -> None:
        self.pos = pos

    def fall(self, dt: float, speed: Vec2) -> None:
        self.pos += dt * speed
