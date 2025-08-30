import random
from pathlib import Path

import pygame

from constants import (
    ASTEROID_IMGS,
    BULLET_HITBOX_SCALE,
    HEALTH_BAR_HEIGHT,
    AsteroidSize,
    ProgramState,
)
from entities.spaceship import Spaceship
from mixins.drawable import Drawable
from mixins.falls import Falls
from mixins.has_health import HasHealth
from utils.tools import scale_hitbox
from utils.vectors import Vec2


class Asteroid(Drawable, Falls, HasHealth):
    def __assign(self, pos: Vec2) -> None:
        img_name = random.choice(ASTEROID_IMGS)

        self.image = pygame.image.load(img_name).convert_alpha()
        self.pos = pos
        self.size = Asteroid.determine_size(img_name)
        self.health = self.size.value
        self.max_health = self.health

    def __init__(self, pos: Vec2) -> None:
        self.__assign(pos)

    def reuse(
        self, pos: Vec2
    ) -> None:  # Some wizardry, limited only if not using super().__init__()
        self.__assign(pos)

    def draw(self, surface: pygame.SurfaceType, state: ProgramState) -> None:
        rect = self.image.get_rect(center=self.pos)
        surface.blit(self.image, rect)

        if self.max_health != self.health:  # Health bar
            self.draw_health_bar(
                surface,
                self.pos - Vec2(self.image.get_size()) // 2,
                Vec2(self.image.get_width(), HEALTH_BAR_HEIGHT),
            )

        if state.DEBUG:
            pygame.draw.rect(surface, (255, 0, 0), scale_hitbox(rect), 1)  # Draw hitbox

    @classmethod
    def determine_size(cls, img_name: str) -> AsteroidSize:
        match Path(img_name).name.split("-")[0].lower():
            case "large":
                return AsteroidSize.LARGE
            case "medium":
                return AsteroidSize.MEDIUM
            case "small":
                return AsteroidSize.SMALL
            case _:
                raise ValueError(f"Unknown image name: {img_name}")

    def collided_with_spaceship(self, spaceship: Spaceship, state: ProgramState):
        a_hitbox = scale_hitbox(self.image.get_rect(center=self.pos))
        s_hitbox = scale_hitbox(spaceship.image.get_rect(center=spaceship.pos))
        if a_hitbox.colliderect(s_hitbox):
            state.GAME_OVER = True

    def collided_with_bullet(self, spaceship: Spaceship) -> None:
        a_hitbox = scale_hitbox(self.image.get_rect(center=self.pos))

        for bullet in spaceship.bullets:
            if a_hitbox.colliderect(
                scale_hitbox(
                    bullet.image.get_rect(center=bullet.pos), BULLET_HITBOX_SCALE
                )
            ):
                self.health -= bullet.damage
                spaceship.bullets.remove(bullet)
