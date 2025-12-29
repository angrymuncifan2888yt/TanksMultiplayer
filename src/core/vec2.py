import math
from dataclasses import dataclass

@dataclass
class Vec2:
    direction: float  # угол в градусах

    @property
    def x(self) -> float:
        rad = math.radians(self.direction)
        return math.cos(rad)

    @property
    def y(self) -> float:
        rad = math.radians(self.direction)
        return -math.sin(rad)  # минус из-за координат Pygame

    def copy(self):
        return Vec2(self.direction)
