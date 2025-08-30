import random

import pygame

from constants import BASE_WIN_SIZE, FONT
from utils.colors import Colors
from utils.vectors import Area, Vec2


def random_top(surface: pygame.SurfaceType) -> Vec2:
    return Vec2(
        random.randint(0, surface.get_width()), random.randint(-surface.get_height(), 0)
    )  # Ensures asteroids don't drop from the same height
    # return Vec2(random.randint(0, surface.get_width()), 0)  # If y doesn't matter


def random_coords(surface: pygame.SurfaceType) -> Vec2:
    return Area(Vec2(), Vec2(surface.get_size())).random_pos()


def items_for_surface(surface: pygame.Surface, base_item_amount: int) -> int:
    return int(base_item_amount * (Vec2(surface.get_size()) / Vec2(BASE_WIN_SIZE)).mult)  # type: ignore


def load_image_scaled(path: str, size: float) -> pygame.Surface:
    img = pygame.image.load(path).convert_alpha()
    return pygame.transform.smoothscale(img, (size, size))


def scale_hitbox(obj: pygame.rect.RectType, scale=(0.8, 0.8)) -> pygame.rect.RectType:
    return obj.scale_by(*scale)


def game_over_screen(surface: pygame.SurfaceType, score: int) -> None:
    msg1 = f"Game Over. Score: {score}"
    msg2 = "Press r to try again"

    font1 = pygame.font.Font(FONT, 64)
    font2 = pygame.font.Font(FONT, 32)

    text1 = font1.render(msg1, True, Colors.WHITE.value())  # white text
    text2 = font2.render(msg2, True, Colors.WHITE.value())  # white text

    pos = Vec2(surface.get_size()) // 2 - Vec2(0, 50)
    rect1 = text1.get_rect(center=pos)
    rect2 = text2.get_rect(center=pos + Vec2(0, 75))

    surface.blit(text1, rect1)
    surface.blit(text2, rect2)


def pause_screen(surface: pygame.SurfaceType) -> None:
    msg1 = "Paused"
    msg2 = "Press p / Esc to continue"

    font1 = pygame.font.Font(FONT, 64)
    font2 = pygame.font.Font(FONT, 32)

    text1 = font1.render(msg1, True, Colors.WHITE.value())  # white text
    text2 = font2.render(msg2, True, Colors.WHITE.value())  # white text

    pos = Vec2(surface.get_size()) // 2 - Vec2(0, 50)
    rect1 = text1.get_rect(center=pos)
    rect2 = text2.get_rect(center=pos + Vec2(0, 75))

    surface.blit(text1, rect1)
    surface.blit(text2, rect2)
