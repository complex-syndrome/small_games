import random

import pygame


class Vec2(pygame.Vector2):
    """_summary_
    A pygame.Vector2 extension, supports arithmethic with ints and floats
    """

    def __sub__(self, other):
        if isinstance(other, int | float):
            return Vec2(self.x - other, self.y - other)
        return Vec2(super().__sub__(other))

    def __rsub__(self, other):
        if isinstance(other, int | float):
            return Vec2(other - self.x, other - self.y)
        return Vec2(super().__rsub__(other))

    def __isub__(self, other):
        if isinstance(other, int | float):
            return Vec2(other - self.x, other - self.y)
        return Vec2(super().__rsub__(other))

    def __add__(self, other):
        if isinstance(other, int | float):
            return Vec2(self.x + other, self.y + other)
        return Vec2(super().__add__(other))

    def __radd__(self, other):
        if isinstance(other, int | float):
            return Vec2(other + self.x, other + self.y)
        return Vec2(super().__radd__(other))

    def __iadd__(self, other):
        if isinstance(other, int | float):
            return Vec2(other + self.x, other + self.y)
        return Vec2(super().__radd__(other))

    def __mul__(self, other):
        if isinstance(other, int | float):
            return Vec2(self.x * other, self.y * other)
        if isinstance(other, pygame.Vector2 | Vec2):
            return Vec2(self.x * other.x, self.y * other.y)
        return NotImplemented

    def __rmul__(self, other):
        if isinstance(other, int | float):
            return Vec2(self.x * other, self.y * other)
        if isinstance(other, pygame.Vector2 | Vec2):
            return Vec2(self.x * other.x, self.y * other.y)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, int | float):
            return Vec2(self.x / other, self.y / other)
        if isinstance(other, pygame.Vector2 | Vec2):
            return Vec2(self.x / other.x, self.y / other.y)
        return NotImplemented

    def __floordiv__(self, other):
        if isinstance(other, int | float):
            return Vec2(self.x // other, self.y // other)
        if isinstance(other, pygame.Vector2 | Vec2):
            return Vec2(self.x // other.x, self.y // other.y)
        return NotImplemented

    def __mod__(self, other):
        if isinstance(other, int | float):
            return Vec2(self.x % other, self.y % other)
        if isinstance(other, pygame.Vector2 | Vec2):
            return Vec2(self.x % other.x, self.y % other.y)
        return NotImplemented

    @property
    def int_tuple(self) -> tuple[int, int]:
        return int(self.x), int(self.y)

    @property
    def mult(self) -> float:
        return self.x * self.y


class Area:
    """_summary_
    start: left_top of area
    end: right_bottom of area
    """

    def __init__(self, start: Vec2, end: Vec2) -> None:
        self.start = start
        self.end = end

    def __str__(self) -> str:
        return f"Start: {self.start}, End: {self.end}"

    def __contains__(self, pos: Vec2) -> bool:
        return (
            self.start.x <= pos.x <= self.end.x and self.start.y <= pos.y <= self.end.y
        )

    def __iter__(self):
        yield self.start
        yield self.end

    @property
    def diff(self) -> Vec2:
        return self.end - self.start

    def random_pos(self) -> Vec2:
        s, e = self.start.int_tuple, self.end.int_tuple
        return Vec2(random.randint(s[0], e[0]), random.randint(s[1], e[1]))
