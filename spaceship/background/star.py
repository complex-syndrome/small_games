import pygame

from constants import ProgramState
from mixins.drawable import Drawable
from mixins.falls import Falls
from utils.colors import ColorValue
from utils.vectors import Vec2


class Star(Drawable, Falls):
    def __assign(self, pos: Vec2, color: ColorValue, size: int) -> None:
        self.pos = pos
        self.color = color
        self.size = size

    def __init__(self, pos: Vec2, color: ColorValue, size: int) -> None:
        self.__assign(pos, color, size)

    def reuse(
        self, pos: Vec2, color: ColorValue, size: int
    ) -> None:  # Some wizardry, limited only if not using super().__init__()
        self.__assign(pos, color, size)

    def draw(self, surface: pygame.SurfaceType, state: ProgramState) -> None:
        pygame.draw.circle(surface, self.color.value(), self.pos, self.size)
