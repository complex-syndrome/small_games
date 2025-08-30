import pygame

from utils.vectors import Vec2


class HasHealth:
    def __init__(self, health: float, max_health: float | None = None) -> None:
        self.health = health
        self.max_health = max_health or health

    def draw_health_bar(self, surface: pygame.SurfaceType, pos: Vec2, size: Vec2):
        x, y = pos
        width, height = size
        ratio = max(0, min(1, self.health / self.max_health))
        pygame.draw.rect(surface, (150, 0, 0), (x, y, width, height))
        pygame.draw.rect(surface, (0, 200, 0), (x, y, int(width * ratio), height))
        pygame.draw.rect(surface, (255, 255, 255), (x, y, width, height), 1)
