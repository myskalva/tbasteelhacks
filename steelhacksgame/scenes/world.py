import pygame
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from characters.player import Player
from scenes.scene import Scene
class World(Scene):
    def __init__(self):
        super().__init__()
        self.player = Player([400, 300], "assets/player2.png")  # your image
        self.all_sprites = pygame.sprite.Group(self.player)

    def update(self, dt, keys):
        self.all_sprites.update(dt, keys)

    def draw(self, screen):
        screen.fill("black")
        self.all_sprites.draw(screen)
