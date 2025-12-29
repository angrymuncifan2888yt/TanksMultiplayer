import pygame
import os


class Sprite:
    OBSTACLE_DURABILITY_2 = None
    OBSTACLE_DURABILITY_1 = None

    @classmethod
    def init(cls):
        cls.OBSTACLE_DURABILITY_1 = pygame.image.load(os.path.join("assets", "img", "durability_1.png"))
        cls.OBSTACLE_DURABILITY_2 = pygame.image.load(os.path.join("assets", "img", "durability_2.png"))