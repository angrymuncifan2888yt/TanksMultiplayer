from dataclasses import dataclass
from world import Tank, Obstacle
from core import Position


@dataclass
class _Map:
    tank1: Tank
    tank2: Tank
    obstacle_list: list


class Maps:
    MAP1 = None
    MAP2 = None

    @classmethod
    def init(cls, world):
        cls.MAP1 = _Map(
            Tank(world, Position(200, 200), (0, 255, 0)),
            Tank(world, Position(600, 600), (255, 0, 0)),
            [Obstacle(world, Position(254, 182), 48, 236),
                    Obstacle(world, Position(249, 583), 58, 124),
                    Obstacle(world, Position(339, 545), 86, 89),
                    Obstacle(world, Position(373, 234), 454, 15),
                    Obstacle(world, Position(373, 274), 86, 89),
                    Obstacle(world, Position(574, 50), 52, 184),
                    Obstacle(world, Position(574, 234), 52, 184),
                    Obstacle(world, Position(373, 234), 454, 15),
                    Obstacle(world, Position(574, 418), 52, 184),
                    Obstacle(world, Position(574, 602), 52, 184),
                    Obstacle(world, Position(373, 234), 454, 15),
                    Obstacle(world, Position(895, 372), 16, 317),
                    Obstacle(world, Position(911, 234), 16, 317),]
        )

        cls.MAP2 = _Map(
            Tank(world, Position(200, 200), (0, 0, 255)),
            Tank(world, Position(600, 600), (255, 0, 255)),
            [Obstacle(world, Position(254, 335), 86, 89),
             Obstacle(world, Position(269, 537), 86, 89),
             Obstacle(world, Position(569, 94), 86, 89),
             Obstacle(world, Position(718, 235), 86, 89),
             Obstacle(world, Position(648, 485), 86, 89),
             Obstacle(world, Position(493, 235), 26, 401),]
        )
