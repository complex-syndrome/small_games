import math

import pygame

from ball import Ball
from colors import ColorValue
from vector import Vec2


class ShrinkCollisionCircleBorder:
    def __init__(
        self, surface, center: Vec2, color: ColorValue, radius: float, width=2
    ) -> None:
        self.__initial_radius = radius
        self.surface = surface
        self.center = center
        self.color = color
        self.radius = radius
        self.width = width

    def reset_border_radius(self):
        self.radius = self.__initial_radius

    def draw(self) -> None:
        pygame.draw.circle(
            self.surface, self.color.value(), self.center, self.radius, self.width
        )

    def shrink(self, shrink_step: float, shrink_limit: float) -> bool:
        if self.radius - shrink_step > shrink_limit:
            self.radius -= shrink_step
            return True
        return False

    def collide(self, ball: Ball, collide_boost=1.0, damping_value=1.0) -> bool:
        (bx, by), (cx, cy) = ball.get_center(), self.center
        dx, dy = bx - cx, by - cy
        dist = math.sqrt(dx * dx + dy * dy)  # Py theorem
        max_dist = self.radius - ball.get_radius()

        if dist > max_dist:  # Edge outside
            nx, ny = dx / dist, dy / dist

            # Clamp inside circle
            ball.set_center(
                self.center[0] + nx * max_dist, self.center[1] + ny * max_dist
            )

            # Bounce
            vx, vy = ball.get_velocity()
            vdn = vx * nx + vy * ny
            vx = (vx - 2 * vdn * nx) * damping_value
            vy = (vy - 2 * vdn * ny) * damping_value

            # Boost
            vx += -nx * collide_boost
            vy += -ny * collide_boost

            # Set
            ball.set_velocity(vx, vy)
            return True

        return False
