from abc import ABC, abstractmethod

import pygame

from constants import ProgramState


class Drawable(ABC):
    @abstractmethod
    def draw(self, surface: pygame.SurfaceType, state: ProgramState):
        pass
