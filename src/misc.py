from dataclasses import dataclass
import pygame
from world import Tank
from dataclasses import dataclass


@dataclass
class ScoreSystem:
    tank1_score: int = 0
    tank2_score: int = 0


@dataclass
class TankController:
    tank: Tank
    turn_left_key: int # pg key
    turn_right_key: int
    move_forward_key: int
    move_backwards_key: int
    shot_key: int

    def control_tank(self, pg_event, delta):
        keys = pygame.key.get_pressed()

        # Movement
        if keys[self.turn_right_key]:
            self.tank.direction.direction -= self.tank.rotation_speed * delta
        if keys[self.turn_left_key]:
            self.tank.direction.direction += self.tank.rotation_speed * delta

        self.tank.direction.direction %= 360

        if keys[self.move_forward_key]:
            self.tank.position.move(self.tank.direction, self.tank.speed, delta)
        if keys[self.move_backwards_key]:
            self.tank.position.move(self.tank.direction, -self.tank.speed * 0.5, delta)

        for event in pg_event:
            if event.type == pygame.KEYDOWN:
                if event.key == self.shot_key:
                    self.tank.shot()
