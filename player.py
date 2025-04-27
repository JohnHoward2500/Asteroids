import pygame
from circleshape import CircleShape
from constants import player_radius, player_turn_speed, player_speed, SHOT_RADIUS, PLAYER_SHOT_SPEED, PLAYER_SHOT_COOLDOWN
from shot import Shot

class Player (CircleShape):
    shot_timer = 0

    def __init__(self, x, y):
        super().__init__(x, y, player_radius)
        self.rotation = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += dt * player_turn_speed

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt * -1)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(dt * -1)
        if keys[pygame.K_SPACE]:
            self.shoot()
        if Player.shot_timer > 0:
            Player.shot_timer -= dt
            

    def shoot(self):
            if Player.shot_timer <= 0:
                shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
                shot.velocity = pygame.math.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOT_SPEED
                Player.shot_timer += PLAYER_SHOT_COOLDOWN

    def move (self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * player_speed * dt
    