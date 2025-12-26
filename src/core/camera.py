from dataclasses import dataclass
from .position import Position

@dataclass
class Camera:
    x: int
    y: int
    width: int
    height: int

    def get_screen_position(self, position: Position):
        return Position(position.x - self.position.x, position.y - self.position.y)

    def center_on_hitbox(self, hitbox):
        center_x = hitbox.position.x + hitbox.width / 2
        center_y = hitbox.position.y + hitbox.height / 2

        self.position.x = center_x - self.width / 2
        self.position.y = center_y - self.height / 2