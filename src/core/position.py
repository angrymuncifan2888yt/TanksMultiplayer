from dataclasses import dataclass


@dataclass
class Position:
    x: int
    y: int
    def move(self, vec2, speed, delta):
        self.x = self.x + vec2.x * (speed * delta)
        self.y = self.y + vec2.y * (speed * delta)

    def copy(self):
        return Position(self.x, self.y)
    
    def __getitem__(self, index: int):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("Position index out of range")