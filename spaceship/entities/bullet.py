import pygame

from constants import BULLET_HITBOX_SCALE, BULLET_IMG, SCALED_BULLET_SIZE, ProgramState
from mixins.drawable import Drawable
from mixins.falls import Falls
from utils.tools import load_image_scaled, scale_hitbox
from utils.vectors import Vec2


class Bullet(Drawable, Falls):
    def __init__(self, pos: Vec2, damage=1) -> None:
        self.image = load_image_scaled(BULLET_IMG, SCALED_BULLET_SIZE)
        self.pos = pos
        self.damage = damage

    def draw(self, surface: pygame.SurfaceType, state: ProgramState) -> None:
        rect = self.image.get_rect(center=self.pos)
        surface.blit(self.image, rect)
        if state.DEBUG:
            pygame.draw.rect(
                surface, (255, 0, 0), scale_hitbox(rect, BULLET_HITBOX_SCALE), 1
            )  # Draw hitbox
