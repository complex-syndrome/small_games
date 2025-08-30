import random


class ColorValue:
    """_summary_
    Just a wrapper for tuple[int, int, int], for pygame rendering.
    """

    def __init__(self, r: int, g: int, b: int) -> None:
        self.r = int(r)
        self.g = int(g)
        self.b = int(b)

        assert 0 <= r <= 255
        assert 0 <= g <= 255
        assert 0 <= b <= 255

    def __str__(self) -> str:
        return f"r: {self.r}, g: {self.g}, b: {self.b}"

    def value(self) -> tuple[int, int, int]:
        return (self.r, self.g, self.b)


class Colors:
    WHITE = ColorValue(255, 255, 255)
    BLACK = ColorValue(0, 0, 0)

    RED = ColorValue(255, 0, 0)
    ORANGE = ColorValue(255, 127, 0)
    YELLOW = ColorValue(255, 255, 0)
    GREEN = ColorValue(0, 255, 0)
    BLUE = ColorValue(0, 0, 255)
    INDIGO = ColorValue(75, 0, 130)
    VIOLET = ColorValue(148, 0, 211)

    MAGENTA = ColorValue(255, 0, 255)
    TEAL = ColorValue(0, 128, 128)

    cur_idx_1 = 0
    cur_idx_2 = 0
    LIGHT_COLORS = (RED, ORANGE, YELLOW, GREEN, TEAL)
    RAINBOW = (RED, ORANGE, YELLOW, GREEN, BLUE, INDIGO, VIOLET)

    @classmethod
    def follow_rainbow(cls) -> ColorValue:
        ret = Colors.RAINBOW[Colors.cur_idx_1]
        Colors.cur_idx_1 = (Colors.cur_idx_1 + 1) % len(Colors.RAINBOW)
        return ret

    @classmethod
    def random_rainbow(cls) -> ColorValue:
        return random.choice(Colors.RAINBOW)

    @classmethod
    def follow_light(cls) -> ColorValue:
        ret = Colors.RAINBOW[Colors.cur_idx_2]
        Colors.cur_idx_2 = (Colors.cur_idx_2 + 1) % len(Colors.LIGHT_COLORS)
        return ret

    @classmethod
    def random_light(cls) -> ColorValue:
        return random.choice(Colors.LIGHT_COLORS)

    @classmethod
    def random_color(cls) -> ColorValue:
        return ColorValue(*[random.randint(0, 255) for _ in range(3)])
