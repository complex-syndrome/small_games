import pygame as pg

from colors import ColorValue
from vector import Vec2


class Ball:
    def __init__(
        self,
        surface: pg.SurfaceType,
        center: Vec2,
        radius: float,
        color: ColorValue,
        g_force: float,
    ) -> None:
        self.surface = surface
        self.set_radius(radius)
        self.set_center(*center)
        self.color = color

        self._velocity = Vec2(0, 0)
        self.g_force: float = g_force

    # Logic
    def out_of_screen(self) -> bool:
        (w, h), (x, y) = self.surface.get_size(), self._center
        return (
            x < -self._radius
            or x > w + self._radius
            or y < -self._radius
            or y > h + self._radius
        )

    def update_gravity(self, dt: float) -> None:
        self._velocity = Vec2(
            self._velocity[0], self._velocity[1] + (self.g_force * dt)
        )
        (x, y), (v1, v2) = self._center, self._velocity
        self.set_center(x + v1, y + v2)

    # Graphics
    def draw(self) -> None:
        pg.draw.circle(self.surface, self.color.value(), self._center, self._radius)

    # Getters / Setters
    def set_center(self, x: float, y: float) -> None:
        self._center = Vec2(x, y)

    def set_velocity(self, vx: float, vy: float) -> None:
        self._velocity = Vec2(vx, vy)

    def clear_velocity(self) -> None:
        self._velocity = Vec2(0, 0)

    def set_radius(self, new_radius: float, border=None) -> None:
        if new_radius <= 0:
            raise ValueError("Invalid radius:", new_radius)
        if border and new_radius >= border.radius:
            return
        self._radius = new_radius

    def get_center(self) -> Vec2:
        return self._center

    def get_radius(self) -> float:
        return self._radius

    def get_velocity(self) -> Vec2:
        return self._velocity
