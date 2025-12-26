from dataclasses import dataclass
from .position import Position

@dataclass
class Hitbox:
    position: Position
    width: int
    height: int

    def collides_hitbox(self, hitbox: "Hitbox"):
        return not (
            self.position.x + self.width < hitbox.position.x or
            self.position.x > hitbox.position.x + hitbox.width or
            self.position.y + self.height < hitbox.position.y or
            self.position.y > hitbox.position.y + hitbox.height
        )

    def handle_collision(self, hitbox: "Hitbox"):
        if not self.collides_hitbox(hitbox):
            return

        dx1 = hitbox.position.x + hitbox.width - self.position.x
        dx2 = self.position.x + self.width - hitbox.position.x
        dy1 = hitbox.position.y + hitbox.height - self.position.y
        dy2 = self.position.y + self.height - hitbox.position.y

        overlap_x = dx1 if dx1 < dx2 else -dx2
        overlap_y = dy1 if dy1 < dy2 else -dy2

        if abs(overlap_x) < abs(overlap_y):
            self.position.x += overlap_x
        else:
            self.position.y += overlap_y
