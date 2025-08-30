from dataclasses import dataclass
from enum import IntEnum

from utils.colors import Colors, ColorValue
from utils.vectors import Vec2


@dataclass
class ProgramState:
    DEBUG: bool = False
    RUNNING: bool = True
    PAUSED: bool = False
    GAME_OVER: bool = False


class AsteroidSize(IntEnum):
    SMALL = 2
    MEDIUM = 3
    LARGE = 5


BASE_WIN_SIZE = (640, 360)  # Or half these
FONT = None
HEALTH_BAR_HEIGHT = 12

BASE_STAR_AMOUNT = 50
STAR_SPEED = Vec2(0, 100)

ASTEROID_IMGS = [
    "assets/large-A.png",
    "assets/large-B.png",
    "assets/medium-A.png",
    "assets/medium-B.png",
    "assets/small-A.png",
    "assets/small-B.png",
]
BASE_ASTEROID_AMOUNT = 3
ASTEROID_SPEED = Vec2(0, 100)


SPACESHIP_IMG = "assets/SpaceShip.png"
SPACESHIP_STEP = 10
SPACESHIP_SCALED_WIDTH = 50


BULLET_IMG = "assets/bullet.png"
SCALED_BULLET_SIZE = 75
BULLET_HITBOX_SCALE = (0.2, 0.8)
SHOOT_BULLET_INTERVAL = 500
BULLET_SPEED = Vec2(0, -200)

# Just background values, doesn't affect gameplay
STAR_SIZES = (1, 3)
bg_color = Colors.BLACK
STAR_COLOR_VARIANTS = [
    ColorValue(200, 200, 255),
    ColorValue(255, 220, 200),
    ColorValue(255, 255, 255),
]
