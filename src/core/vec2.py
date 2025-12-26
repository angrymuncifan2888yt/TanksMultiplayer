import math
from dataclasses import dataclass


@dataclass
class Vec2:
    direction: float

    @property
    def x(self) -> float:
        rad = math.radians(self.direction)
        return math.cos(rad)

    @property
    def y(self) -> float:
        rad = math.radians(self.direction)
        return -math.sin(rad)
