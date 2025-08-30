import random
import sys

import pygame


def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i : i + 2], 16) for i in (0, 2, 4))


FPS = 60
WIDTH, HEIGHT = 500, 500
CELL_SIZE = 10
ROWS, COLS = WIDTH // CELL_SIZE, HEIGHT // CELL_SIZE
GRID = [[0 for _ in range(COLS)] for _ in range(ROWS)]

COLORS = ["#7a7a7a", "#ffff66", "#99ff33"]
COLOR_INDEX = 0
COLOR_RANDOMIZE = False

BORDER_COLOR = (25, 25, 25)
DEAD_COLOR = (255, 255, 255)
ALIVE_COLOR = hex_to_rgb(COLORS[COLOR_INDEX])

CHANGE_INTERVAL_MIN = 500
CHANGE_INTERVAL = 500
RANDOM_FILL_BLOCK_PROB = 0.2

MOUSE_DOWN = False
CLEAR_BOARD = False
RUNNING = True
PAUSED = False
STEP_ONCE = False


def display_init() -> pygame.Surface:
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Conway's Game of Life")

    return screen


def read_event(event: pygame.event.Event) -> None:
    global \
        COLOR_RANDOMIZE, \
        PAUSED, \
        RUNNING, \
        MOUSE_DOWN, \
        STEP_ONCE, \
        CHANGE_INTERVAL, \
        CLEAR_BOARD

    match event.type:
        case pygame.QUIT:
            RUNNING = False

        case pygame.MOUSEBUTTONDOWN:
            if not PAUSED:
                MOUSE_DOWN = True
                row, col = (_ // CELL_SIZE for _ in pygame.mouse.get_pos())
                if in_board(row, col):
                    toggle_state(row, col)

        case pygame.MOUSEBUTTONUP:
            MOUSE_DOWN = False

        case pygame.KEYDOWN:
            match event.key:
                case pygame.K_SPACE:
                    PAUSED = not PAUSED
                    print(f"Game {'un' if not PAUSED else ''}paused.")

                case pygame.K_r:  # Toggle COLOR_RANDOMIZE
                    COLOR_RANDOMIZE = not COLOR_RANDOMIZE
                    s = "ON" if COLOR_RANDOMIZE else "OFF"
                    print(f"Color Randomization is currently: {s}")

                case pygame.K_s:
                    if not PAUSED:
                        PAUSED = True
                    STEP_ONCE = True
                    print("Next step generated.")

                case pygame.K_x:  # Invert board
                    for row in range(ROWS):
                        for col in range(COLS):
                            toggle_state(row, col)
                    print("Color of board inverted.")

                case pygame.K_c:  # Change color
                    change_activated_color()

                case pygame.K_z:
                    for row in range(ROWS):
                        for col in range(COLS):
                            if random.random() < RANDOM_FILL_BLOCK_PROB:
                                toggle_state(row, col)
                    print("Random filled blocks.")

                case pygame.K_v:
                    for row in range(ROWS):
                        for col in range(COLS):
                            GRID[row][col] = 0
                    CHANGE_INTERVAL = CHANGE_INTERVAL_MIN
                    print("Board cleared and speed resetted.")

                case pygame.K_MINUS:
                    CHANGE_INTERVAL = (
                        CHANGE_INTERVAL - 500
                        if CHANGE_INTERVAL > CHANGE_INTERVAL_MIN
                        else CHANGE_INTERVAL
                    )
                    print(f"Speed increased. ({CHANGE_INTERVAL}) [Minimum 0.5 secs]")

                case pygame.K_EQUALS:
                    CHANGE_INTERVAL += 500
                    print(f"Speed decreased. ({CHANGE_INTERVAL}) [Minimum 0.5 secs]")

    if MOUSE_DOWN:
        row, col = (_ // CELL_SIZE for _ in pygame.mouse.get_pos())
        if in_board(row, col):
            toggle_state(row, col)


def in_board(row: int, col: int) -> bool:
    return 0 <= row < ROWS and 0 <= col < COLS


def toggle_state(row: int, col: int) -> None:
    GRID[col][row] = 1 - GRID[col][row]


def change_activated_color() -> None:
    global COLOR_INDEX, ALIVE_COLOR

    if COLOR_RANDOMIZE:
        new_color = tuple(random.randint(0, 255) for _ in range(3))
    else:
        COLOR_INDEX = (COLOR_INDEX + 1) % len(COLORS)
        new_color = hex_to_rgb(COLORS[COLOR_INDEX])
    ALIVE_COLOR = new_color


def game_start() -> None:
    global GRID, STEP_ONCE, CLEAR_BOARD
    screen = display_init()
    clock = pygame.time.Clock()
    last_change_interval = pygame.time.get_ticks()

    while RUNNING:
        now = pygame.time.get_ticks()
        for event in pygame.event.get():
            read_event(event)

        if (not PAUSED and now - last_change_interval >= CHANGE_INTERVAL) or STEP_ONCE:
            GRID = calculate_next_gen()
            last_change_interval = now
            STEP_ONCE = False

        draw_board(screen)
        pygame.display.flip()
        clock.tick(FPS)


def draw_grid_lines(screen: pygame.Surface) -> None:
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, BORDER_COLOR, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, BORDER_COLOR, (0, y), (WIDTH, y))


def draw_board(screen: pygame.Surface) -> None:
    for row in range(ROWS):
        for col in range(COLS):
            color = ALIVE_COLOR if GRID[row][col] else DEAD_COLOR
            rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, color, rect)

    draw_grid_lines(screen)


def count_neighbours(r, c) -> int:
    total = 0
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == dc == 0:
                continue
            nr, nc = r + dr, c + dc
            if in_board(nr, nc):
                total += GRID[nr][nc]
    return total


def calculate_next_gen() -> list[list[int]]:
    new_grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]
    for r in range(ROWS):
        for c in range(COLS):
            n_count = count_neighbours(r, c)
            if (GRID[r][c] == 1 and n_count in [2, 3]) or (
                GRID[r][c] == 0 and n_count == 3
            ):
                new_grid[r][c] = 1
    return new_grid


def main() -> None:
    pygame.init()
    game_start()
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
