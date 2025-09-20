import pygame

from scenes.scene import Scene

class World(Scene):
    def __init__(self):
        self.player_pos = [400, 300]

    def update(self, dt, keys):
        speed = 200
        if keys[pygame.K_w]: self.player_pos[1] -= speed * dt
        if keys[pygame.K_s]: self.player_pos[1] += speed * dt
        if keys[pygame.K_a]: self.player_pos[0] -= speed * dt
        if keys[pygame.K_d]: self.player_pos[0] += speed * dt

    def draw(self, screen):
        screen.fill("black")
        pygame.draw.circle(screen, "red", self.player_pos, 20)
