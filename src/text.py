from core import Position
import pygame


class Text:
    def __init__(self, text: str, position: Position,
                 font: pygame.font.Font, color: tuple[int, int, int]=(255, 255, 255)):
        self.__text = text
        self.__position = position
        self.__font = font
        self.__color = color

    @property
    def text(self) -> str:
        return self.__text
    
    @text.setter
    def text(self, value: str):
        self.__text = value

    @property
    def position(self) -> Position:
        return self.__position
    
    @position.setter
    def position(self, value: Position):
        self.__position = value

    @property
    def color(self) -> tuple[int, int, int]:
        return self.__color
    
    @color.setter
    def color(self, value: tuple[int, int, int]):
        self.__color = value

    @property
    def font(self) -> pygame.font.Font:
        return self.__font

    def center_by_x(self, screen_width: int):
        text_width = self.font.size(self.text)[0]
        self.position.x = (screen_width - text_width) / 2

    def center_in_hitbox(self, hitbox):
        w, h = self.font.size(self.text)
        self.position.x = hitbox.position.x + (hitbox.width - w) / 2
        self.position.y = hitbox.position.y + (hitbox.height - h) / 2