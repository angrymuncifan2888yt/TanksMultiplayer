import pygame
from world import World
from renderer import RendererEntity, RendererText
from assets import Sprite, Maps, Fonts
from misc import TankController, ScoreSystem
from const import ScreenSize
from core import Position
from text import Text
import sys
import random


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.font.init()
        Sprite.init()
        Fonts.init()

        self.screen = pygame.display.set_mode((ScreenSize.WIDTH, ScreenSize.HEIGHT))
        pygame.display.set_caption("Tanks multiplayer")
        self.clock = pygame.time.Clock()

        self.create_world()
        self.score = ScoreSystem()
        self.tank1_score_text = Text(str(self.score.tank1_score), Position(100, 100), Fonts.FONT_30, self.tank1.color)
        self.tank2_score_text = Text(str(self.score.tank2_score), Position(1000, 100), Fonts.FONT_30, self.tank2.color)

    def create_world(self):
        # World/Tanks
        self.world = World()
        Maps.init(self.world)
        current_map = random.choice([Maps.MAP1, Maps.MAP2])
        self.tank1 = current_map.tank1
        self.tank2 = current_map.tank2
        self.world.add_entity(self.tank1)
        self.world.add_entity(self.tank2)
        
        for ent in current_map.obstacle_list:
            self.world.add_entity(ent)
        
        # Tanks controllers
        self.tank1_controller = TankController(self.tank1, pygame.K_a,
                                               pygame.K_d, pygame.K_w,
                                               pygame.K_s, pygame.K_SPACE)
        self.tank2_controller = TankController(self.tank2, pygame.K_j,
                                               pygame.K_l, pygame.K_i,
                                               pygame.K_k, pygame.K_RETURN)

    def mainloop(self):
        while True:
            pygame.display.update()
            self.screen.fill((0, 0,0))
            delta = self.clock.tick(60) / 1000
            pg_event = pygame.event.get()

            # Input
            self.tank1_controller.control_tank(pg_event, delta)
            self.tank2_controller.control_tank(pg_event, delta)
            # Logic
            self.tank1_score_text.text = str(self.score.tank1_score)
            self.tank2_score_text.text = str(self.score.tank2_score)
            self.tank1_score_text.color = self.tank1.color
            self.tank2_score_text.color = self.tank2.color
            self.world.update(delta)

            if not self.tank1.is_alive or not self.tank2.is_alive:
                if self.tank1.is_alive:
                    self.score.tank1_score += 1
                else:
                    self.score.tank2_score += 2
                self.create_world()

            # Render
            for entity in self.world.entity_list:
                RendererEntity.render(self.screen, entity)
            
            RendererText.render(self.screen, self.tank1_score_text)
            RendererText.render(self.screen, self.tank2_score_text)

            for event in pg_event:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)

if __name__ == "__main__":
    game = Game()
    game.mainloop()