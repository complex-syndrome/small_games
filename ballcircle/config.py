from dataclasses import dataclass

from vector import Area, Vec2


@dataclass
class SimulationConfig:
    window_size = Vec2(800, 800)
    window_title = "A circle and many balls."
    ball_size = 10

    circle_shrink_step = 1
    ball_expand_step = 1

    g_force = 20

    initial_circle_radius = (min(window_size) - 100) / 2
    spawn_range_from_center = initial_circle_radius // 2

    @property
    def center(self) -> Vec2:
        return self.window_size // 2

    @property
    def spawn_area(self) -> Area:
        return Area(
            Vec2(self.center - self.spawn_range_from_center),
            Vec2(self.center + self.spawn_range_from_center),
        )
