import pygame
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

tank_img = pygame.Surface((50, 30), pygame.SRCALPHA)
pygame.draw.rect(tank_img, (0, 255, 0), (0, 0, 50, 30))

bullet_img = pygame.Surface((10, 5), pygame.SRCALPHA)
pygame.draw.rect(bullet_img, (255, 0, 0), (0, 0, 10, 5))

class Tank:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 0
        self.speed = 0
        self.rotation_speed = 0
        self.max_speed = 5
        self.acceleration = 0.2
        self.friction = 0.1

    def update(self):
        self.angle += self.rotation_speed
        rad = math.radians(self.angle)
        self.x += self.speed * math.cos(rad)
        self.y -= self.speed * math.sin(rad)
        if self.speed > 0:
            self.speed -= self.friction
        elif self.speed < 0:
            self.speed += self.friction
        if abs(self.speed) < self.friction:
            self.speed = 0

    def draw(self, surface):
        rotated_image = pygame.transform.rotate(tank_img, self.angle)
        rect = rotated_image.get_rect(center=(self.x, self.y))
        surface.blit(rotated_image, rect.topleft)

class Bullet:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = 10

    def update(self):
        rad = math.radians(self.angle)
        self.x += self.speed * math.cos(rad)
        self.y -= self.speed * math.sin(rad)

    def draw(self, surface):
        rotated_image = pygame.transform.rotate(bullet_img, self.angle)
        rect = rotated_image.get_rect(center=(self.x, self.y))
        surface.blit(rotated_image, rect.topleft)

tank = Tank(WIDTH//2, HEIGHT//2)
bullets = []

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append(Bullet(tank.x, tank.y, tank.angle))

    keys = pygame.key.get_pressed()
    tank.rotation_speed = 0
    if keys[pygame.K_a]:
        tank.rotation_speed = 5
    if keys[pygame.K_d]:
        tank.rotation_speed = -5
    if keys[pygame.K_w]:
        tank.speed += tank.acceleration
        if tank.speed > tank.max_speed:
            tank.speed = tank.max_speed
    if keys[pygame.K_s]:
        tank.speed -= tank.acceleration
        if tank.speed < -tank.max_speed:
            tank.speed = -tank.max_speed

    tank.update()
    for b in bullets:
        b.update()

    screen.fill((0, 0, 0))
    tank.draw(screen)
    for b in bullets:
        b.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
