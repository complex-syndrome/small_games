import random
import sys

import pygame

from background.star import Star
from constants import (
    ASTEROID_SPEED,
    BASE_ASTEROID_AMOUNT,
    BASE_STAR_AMOUNT,
    BASE_WIN_SIZE,
    SPACESHIP_STEP,
    STAR_COLOR_VARIANTS,
    STAR_SIZES,
    STAR_SPEED,
    ProgramState,
)
from entities.asteroid import Asteroid
from entities.spaceship import Spaceship
from utils.colors import Colors, TextColor
from utils.tools import (
    game_over_screen,
    items_for_surface,
    pause_screen,
    random_coords,
    random_top,
)
from utils.vectors import Vec2

# Base configs
SURFACE = pygame.display.set_mode(BASE_WIN_SIZE, pygame.RESIZABLE)
CLOCK = pygame.time.Clock()
STATE = ProgramState()

# Objects
stars: list[Star] = []
asteriods: list[Asteroid] = []
spaceship: Spaceship


def reset_game() -> None:
    global stars, asteriods, spaceship
    stars = [
        Star(
            random_coords(SURFACE),
            random.choice(STAR_COLOR_VARIANTS),
            random.randint(*STAR_SIZES),
        )
        for _ in range(items_for_surface(SURFACE, BASE_STAR_AMOUNT))
    ]
    asteriods = [
        Asteroid(random_top(SURFACE))
        for _ in range(items_for_surface(SURFACE, BASE_ASTEROID_AMOUNT))
    ]
    spaceship = Spaceship(Vec2(SURFACE.get_size()) // 2, "Spaceship")


def start() -> None:
    reset_game()

    while STATE.RUNNING:
        dt = CLOCK.tick(60) / 1000  # Time
        SURFACE.fill(Colors.BLACK.value())  # bg
        for event in pygame.event.get():
            match_event(event)  # Controls

        if STATE.GAME_OVER:
            game_over_screen(SURFACE, spaceship.score)

        elif STATE.PAUSED:
            pause_screen(SURFACE)

        else:
            # Keys to move
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                spaceship.move(Vec2(-SPACESHIP_STEP, 0), SURFACE)
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                spaceship.move(Vec2(SPACESHIP_STEP, 0), SURFACE)
            if keys[pygame.K_UP] or keys[pygame.K_w]:
                spaceship.move(Vec2(0, -SPACESHIP_STEP), SURFACE)
            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                spaceship.move(Vec2(0, SPACESHIP_STEP), SURFACE)

            # star
            for star in stars:
                star.draw(SURFACE, STATE)
                star.fall(dt, STAR_SPEED)
                if star.pos.y > SURFACE.get_height():
                    star.reuse(
                        random_top(SURFACE),
                        random.choice(STAR_COLOR_VARIANTS),
                        random.randint(*STAR_SIZES),
                    )

            # asteroid
            for asteriod in asteriods:
                asteriod.draw(SURFACE, STATE)
                asteriod.fall(dt, ASTEROID_SPEED)

                asteriod.collided_with_bullet(spaceship)
                if asteriod.health <= 0:
                    spaceship.score += 1

                if (
                    asteriod.pos.y - asteriod.image.get_height() > SURFACE.get_height()
                    or asteriod.health <= 0
                ):
                    asteriod.reuse(random_top(SURFACE))

                asteriod.collided_with_spaceship(spaceship, STATE)

            # spaceship
            spaceship.shoot_bullets(SURFACE, STATE, dt)
            spaceship.draw(SURFACE, STATE)
            spaceship.draw_score(SURFACE)

        # Refresh next scene
        pygame.display.flip()


def match_event(event) -> None:
    global stars, asteriods
    match event.type:
        case pygame.QUIT:
            STATE.RUNNING = False

        case pygame.VIDEORESIZE:
            # Refresh elements to fit new window size
            stars = [
                Star(
                    random_coords(SURFACE),
                    random.choice(STAR_COLOR_VARIANTS),
                    random.randint(*STAR_SIZES),
                )
                for _ in range(items_for_surface(SURFACE, BASE_STAR_AMOUNT))
            ]
            asteriods = [
                Asteroid(random_top(SURFACE))
                for _ in range(items_for_surface(SURFACE, BASE_ASTEROID_AMOUNT))
            ]

        case pygame.KEYDOWN:
            match event.key:
                case pygame.K_r:
                    reset_game()
                    STATE.PAUSED = False
                    STATE.GAME_OVER = False
                    if STATE.DEBUG:
                        print(TextColor.color_it("Game restarted.", TextColor.GREEN))

                case pygame.K_p:
                    pause()

                case pygame.K_ESCAPE:
                    pause()


def pause():
    STATE.PAUSED = not STATE.PAUSED
    if STATE.DEBUG:
        print(
            TextColor.color_it(
                f"Game {'un' if not STATE.PAUSED else ''}paused.",
                TextColor.YELLOW,
            )
        )


def main() -> None:
    pygame.init()
    start()
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
