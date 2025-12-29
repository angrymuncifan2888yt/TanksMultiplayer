import pygame
import os


class Fonts:
    FONT_30 = None

    @classmethod
    def init(cls):
        cls.FONT_30 = pygame.font.Font(os.path.join("assets", "font", "GameFont.ttf"), 30)
        