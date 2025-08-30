import pygame

from constants import (
    BULLET_SPEED,
    FONT,
    SHOOT_BULLET_INTERVAL,
    SPACESHIP_IMG,
    SPACESHIP_SCALED_WIDTH,
    ProgramState,
)
from entities.bullet import Bullet
from mixins.drawable import Drawable
from utils.colors import Colors
from utils.tools import load_image_scaled, scale_hitbox
from utils.vectors import Vec2


class Spaceship(Drawable):
    def __init__(self, pos: Vec2, name: str) -> None:
        self.image = load_image_scaled(SPACESHIP_IMG, SPACESHIP_SCALED_WIDTH)
        self.pos = pos
        self.name = name
        self.color = Colors.WHITE

        self.last_bullet_interval = pygame.time.get_ticks()
        self.bullets: list[Bullet] = []
        self.score = 0

    # Wrap horizontal only
    def move(self, delta: Vec2, surface: pygame.SurfaceType) -> None:
        self.pos += delta
        w, h = surface.get_size()
        self.pos.x %= w
        self.pos.y = max(0, min(self.pos.y, h))
        # self.pos = (self.pos + delta) % Vec2(surface.get_size())   # Wrap all

    def draw(self, surface: pygame.SurfaceType, state: ProgramState) -> None:
        rect = self.image.get_rect(center=self.pos)
        surface.blit(self.image, rect)
        if state.DEBUG:
            pygame.draw.rect(surface, (255, 0, 0), scale_hitbox(rect), 1)  # Draw hitbox

    def shoot_bullets(
        self, surface: pygame.SurfaceType, state: ProgramState, dt: float
    ) -> None:
        now = pygame.time.get_ticks()
        if now - self.last_bullet_interval >= SHOOT_BULLET_INTERVAL:  # Timeout
            self.last_bullet_interval = now
            self.bullets.append(Bullet(self.pos - Vec2(0, 20)))
        self.display_and_move_bullets(surface, state, dt)

    def display_and_move_bullets(
        self, surface: pygame.SurfaceType, state: ProgramState, dt: float
    ) -> None:
        for bullet in self.bullets:
            bullet.draw(surface, state)
            bullet.fall(dt, BULLET_SPEED)
            if bullet.pos.y + bullet.image.get_height() < 0:
                self.bullets.remove(bullet)  # Out of screen

    def draw_score(self, surface: pygame.SurfaceType) -> None:
        text_surface = pygame.font.Font(FONT, 30).render(
            f"Score: {self.score}", True, self.color.value()
        )
        surface.blit(text_surface, (10, 10))
