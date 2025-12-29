from core import Vec2
from core import Hitbox
from core import Position
from const import ScreenSize


class Entity:
    def __init__(self, world, position, width, height):
        super().__init__()
        self.hitbox = Hitbox(position, width, height)
        self.world = world
        self.is_alive = True

    def update(self, delta):
        pass

    @property
    def position(self):
        return self.hitbox.position
    
    @position.setter
    def position(self, value):
        self.hitbox.position = value

    def onCollision(self, entity):
        pass


class Obstacle(Entity):
    def __init__(self, world, position, width=250, height=50):
        super().__init__(world, position, width, height)
        self.durability = 3

    def update(self, delta):
        if self.durability <= 0:
            self.world.remove_entity(self)
              
    def onCollision(self, entity):
        if isinstance(entity, Bullet):
            self.durability -= 1
            self.world.remove_entity(entity)


class Bullet(Entity):
    def __init__(self, world, position, direction, source=None):
        super().__init__(world, position, 10, 10)
        self.direction = direction
        self.source = source

    def update(self, delta):
        self.position.move(self.direction, 1000, delta)

class Border(Entity):
    def __init__(self, world, position, width, height):
        super().__init__(world, position, width, height)
    
    def onCollision(self, entity):
        if isinstance(entity, Bullet):
            self.world.remove_entity(entity)
        
        elif isinstance(entity, Border):
            pass

        else:
            entity.hitbox.handle_collision(self.hitbox)


class Tank(Entity):
    def __init__(self, world, pos, color):
        super().__init__(world, pos, 100, 25)
        self.color = color
        self.speed = 350  # Pixels per second
        self.rotation_speed = 200
        self.direction = Vec2(0)

    def shot(self):
        center_x = self.position.x + self.hitbox.width / 2
        center_y = self.position.y + self.hitbox.height / 2

        spawn_x = center_x + self.direction.x
        spawn_y = center_y + self.direction.y

        bullet_pos = self.position.copy()
        bullet_pos.x = spawn_x
        bullet_pos.y = spawn_y

        self.world.add_entity(Bullet(self.world, bullet_pos, self.direction.copy(), self))

    def onCollision(self, entity):
        if isinstance(entity, Obstacle):
            self.hitbox.handle_collision(entity.hitbox)

        elif isinstance(entity, Bullet):
            if entity.source != self:
                self.world.remove_entity(self)

class World:
    def __init__(self):
        self.entity_list = []

        # World borders
        left_border = Border(self, Position(0, 0), 50, ScreenSize.HEIGHT)
        right_border = Border(self, Position(ScreenSize.WIDTH, 0), 50, ScreenSize.HEIGHT)
        right_border.position.x -= right_border.hitbox.width
        top_border = Border(self, Position(0, 0), ScreenSize.WIDTH, 50)
        down_border = Border(self, Position(0, ScreenSize.HEIGHT), ScreenSize.WIDTH, 50)
        down_border.position.y -= down_border.hitbox.height
        self.add_entity(left_border)
        self.add_entity(right_border)
        self.add_entity(top_border)
        self.add_entity(down_border)

    def add_entity(self, entity):
        self.entity_list.append(entity)

    def remove_entity(self, entity):
        entity.is_alive = False
            
    def update(self, delta):
        copy_ = self.entity_list.copy()
        for entity in copy_:      
            if not entity.is_alive:
                self.entity_list.remove(entity)
                continue

            entity.update(delta)

            # Collision
            for othr in copy_:
                if othr != entity and othr.hitbox.collides_hitbox(entity.hitbox):
                    entity.onCollision(othr)
            