import pygame
from assets import Sprite
from world import Bullet, Tank, Obstacle, Border


class _RendererBullet:
    @staticmethod
    def render(screen: pygame.Surface, bullet, camera=None):
        bullet_pos = camera.get_screen_position(bullet.position) if camera else bullet.position
        bullet_surface = pygame.Surface((bullet.hitbox.width, bullet.hitbox.height))
        bullet_surface.fill((255, 0, 0))
        screen.blit(bullet_surface, (bullet_pos.x, bullet_pos.y))


class _RendererBorder:
    @staticmethod
    def render(screen: pygame.Surface, border, camera=None):
        border_pos = camera.get_screen_position(border.position) if camera else border.position
        border_surface = pygame.Surface((border.hitbox.width, border.hitbox.height))
        border_surface.fill((0, 255, 255))
        screen.blit(border_surface, (border_pos.x, border_pos.y))


class _RendererTank:
    @staticmethod
    def render(screen: pygame.Surface, tank, camera=None):
        pos = camera.get_screen_position(tank.position) if camera else tank.position

        base = pygame.Surface(
            (tank.hitbox.width, tank.hitbox.height),
            pygame.SRCALPHA
        )
        base.fill(tank.color)

        rotated = pygame.transform.rotate(base, tank.direction.direction)

        center = (
            pos.x + tank.hitbox.width / 2,
            pos.y + tank.hitbox.height / 2
        )

        rect = rotated.get_rect(center=center)
        screen.blit(rotated, rect.topleft)


class _RendererObstacle:
    scaled_sprites_cache = {}

    @staticmethod
    def get_scaled_sprite(durability, width, height):
        key = (durability, width, height)
        if key not in _RendererObstacle.scaled_sprites_cache:
            if durability == 2:
                sprite = Sprite.OBSTACLE_DURABILITY_2
            elif durability == 1:
                sprite = Sprite.OBSTACLE_DURABILITY_1
            _RendererObstacle.scaled_sprites_cache[key] = pygame.transform.scale(sprite, (width, height))
        return _RendererObstacle.scaled_sprites_cache[key]

    @staticmethod
    def render(screen: pygame.Surface, obstacle, camera=None):
        obstacle_pos = camera.get_screen_position(obstacle.position) if camera else obstacle.position
        surf = pygame.Surface((obstacle.hitbox.width, obstacle.hitbox.height))
        surf.fill((255, 255, 255))
        screen.blit(surf, (obstacle_pos.x, obstacle_pos.y))

        if 0 < obstacle.durability < 3:
            sprite = _RendererObstacle.get_scaled_sprite(obstacle.durability, obstacle.hitbox.width, obstacle.hitbox.height)
            screen.blit(sprite, (obstacle_pos.x, obstacle_pos.y))


class RendererEntity:
    ENTITY_RENDERERS = {
        Bullet: _RendererBullet,
        Tank: _RendererTank,
        Obstacle: _RendererObstacle,
        Border: _RendererBorder,
    }

    @staticmethod
    def render(screen, entity, camera=None):
        RendererEntity.ENTITY_RENDERERS[type(entity)].render(screen, entity, camera)


import pygame


class RendererText:
    @staticmethod
    def render(
        surface: pygame.Surface,
        text,
        camera: None = None
    ):
        text_surface = text.font.render(
            text.text,
            True,
            text.color
        )

        if camera:
            pos = camera.get_screen_position(text.position)
            surface.blit(text_surface, (pos.x, pos.y))
        else:
            surface.blit(
                text_surface,
                (text.position.x, text.position.y)
            )