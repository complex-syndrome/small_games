import random


class ColorValue:
    """_summary_
    Just a wrapper for tuple[int, int, int], for pygame rendering.
    """

    MIN_COLOR = 0
    MAX_COLOR = 255

    def __init__(self, r: int, g: int, b: int) -> None:
        self.r = int(r)
        self.g = int(g)
        self.b = int(b)

        assert ColorValue.MIN_COLOR <= r <= ColorValue.MAX_COLOR
        assert ColorValue.MIN_COLOR <= g <= ColorValue.MAX_COLOR
        assert ColorValue.MIN_COLOR <= b <= ColorValue.MAX_COLOR

    def __str__(self) -> str:
        return f"r: {self.r}, g: {self.g}, b: {self.b}"

    def __iter__(self):
        yield self.r
        yield self.g
        yield self.b

    def __mul__(self, other):
        if isinstance(other, int | float):
            return ColorValue(
                int(self.r * other), int(self.g * other), int(self.b * other)
            )
        if isinstance(other, ColorValue):
            return ColorValue(self.r * other.r, self.g * other.g, self.g * other)
        return NotImplemented

    def __rmul__(self, other):
        if isinstance(other, int | float):
            return ColorValue(
                int(self.r * other), int(self.g * other), int(self.b * other)
            )
        if isinstance(other, ColorValue):
            return ColorValue(self.r * other.r, self.g * other.g, self.g * other)
        return NotImplemented

    def value(self) -> tuple[int, int, int]:
        return (self.r, self.g, self.b)


class Colors:
    sky_blue = ColorValue(113, 188, 225)
    light_grass = ColorValue(156, 212, 92)
    dark_grass = ColorValue(115, 168, 59)
    mountain_gray = ColorValue(105, 105, 105)

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

    cur_idx = 0
    RAINBOW = (RED, ORANGE, YELLOW, GREEN, BLUE, INDIGO, VIOLET)

    @classmethod
    def follow_rainbow(cls) -> ColorValue:
        ret = Colors.RAINBOW[Colors.cur_idx]
        Colors.cur_idx = (Colors.cur_idx + 1) % len(Colors.RAINBOW)
        return ret

    @classmethod
    def random_rainbow(cls) -> ColorValue:
        return random.choice(Colors.RAINBOW)

    @classmethod
    def random_color(cls) -> ColorValue:
        return ColorValue(*[random.randint(0, 255) for _ in range(3)])


class TextColor:
    """_summary_
    Some colors for cli printing.
    """

    RESET = "\033[0m"
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"

    @classmethod
    def color_it(cls, message: str, color: str) -> str:
        return f"{color}{message}{TextColor.RESET}"
