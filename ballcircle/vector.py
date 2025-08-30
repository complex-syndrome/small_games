import random

import pygame as pg


class Vec2(pg.Vector2):
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

    def __add__(self, other):
        if isinstance(other, int | float):
            return Vec2(self.x + other, self.y + other)
        return Vec2(super().__add__(other))

    def __radd__(self, other):
        if isinstance(other, int | float):
            return Vec2(other + self.x, other + self.y)
        return Vec2(super().__radd__(other))

    def __mul__(self, other):
        if isinstance(other, int | float):
            return Vec2(self.x * other, self.y * other)
        if isinstance(other, pg.Vector2 | Vec2):
            return Vec2(self.x * other.x, self.y * other.y)
        return NotImplemented

    def __rmul__(self, other):
        if isinstance(other, int | float):
            return Vec2(self.x * other, self.y * other)
        if isinstance(other, pg.Vector2 | Vec2):
            return Vec2(self.x * other.x, self.y * other.y)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, int | float):
            return Vec2(self.x / other, self.y / other)
        if isinstance(other, pg.Vector2 | Vec2):
            return Vec2(self.x / other.x, self.y / other.y)
        return NotImplemented

    def __floordiv__(self, other):
        if isinstance(other, int | float):
            return Vec2(self.x // other, self.y // other)
        if isinstance(other, pg.Vector2 | Vec2):
            return Vec2(self.x // other.x, self.y // other.y)
        return NotImplemented

    @property
    def int_tuple(self) -> tuple[int, int]:
        return int(self.x), int(self.y)


class Area:
    """_summary_
    start: left_top of area
    end: right_bottom of area
    """

    def __init__(self, start: Vec2, end: Vec2) -> None:
        self.start = start
        self.end = end

    def __contains__(self, pos: Vec2):
        return self.start.x < pos.x < self.end.x and self.start.y < pos.y < self.end.y

    def __iter__(self):
        yield self.start
        yield self.end

    def diff(self) -> Vec2:
        return self.end - self.start

    def random(self) -> Vec2:
        return Vec2([random.uniform(c1, c2) for c1, c2 in zip(self.start, self.end)])
