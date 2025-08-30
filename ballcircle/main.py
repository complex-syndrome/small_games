import sys

import pygame as pg

from ball import Ball
from border import ShrinkCollisionCircleBorder
from colors import Colors
from config import SimulationConfig
from state import ProgramState
from vector import Vec2

CONFIG = SimulationConfig()
STATE = ProgramState()
SURFACE = pg.display.set_mode(CONFIG.window_size)
CLOCK = pg.time.Clock()
pg.display.set_caption(CONFIG.window_title)

shrinking_circle = ShrinkCollisionCircleBorder(
    SURFACE, CONFIG.center, Colors.WHITE, CONFIG.initial_circle_radius
)


def get_random_ball(position=None) -> Ball:
    return Ball(
        SURFACE,
        position or CONFIG.spawn_area.random(),
        CONFIG.ball_size,
        Colors.follow_light(),
        CONFIG.g_force,
    )


balls: list[Ball] = []


def start_sim() -> None:
    while STATE.RUNNING:
        for event in pg.event.get():
            match_event(event)

        if STATE.PAUSED:
            continue

        dt = CLOCK.tick(60) / 1000  # delta time per sec
        SURFACE.fill(Colors.BLACK.value())
        shrinking_circle.draw()

        for ball in balls:
            ball.update_gravity(dt)
            if shrinking_circle.collide(ball):
                shrinking_circle.shrink(CONFIG.circle_shrink_step, ball.get_radius())
                ball.set_radius(
                    ball.get_radius() + CONFIG.ball_expand_step, shrinking_circle
                )
            ball.draw()

        pg.display.flip()


def match_event(event) -> None:
    match event.type:
        case pg.QUIT:
            STATE.RUNNING = False
        case pg.KEYDOWN:
            match event.key:
                case pg.K_p:
                    STATE.PAUSED = not STATE.PAUSED
                    print(f"\nShrinking {'paused' if STATE.PAUSED else 'continued'}.")

                case pg.K_r:
                    shrinking_circle.reset_border_radius()
                    STATE.LOGGED = False
                    balls.clear()
                    print("\nProgram resetted.")

                case pg.K_b:
                    balls.append(get_random_ball())

        case pg.MOUSEBUTTONDOWN:
            balls.append(get_random_ball(Vec2(event.pos)))


def main():
    pg.init()
    start_sim()
    pg.quit()
    sys.exit()


if __name__ == "__main__":
    main()
