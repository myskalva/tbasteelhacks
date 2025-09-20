import pygame
from scenes.scene import Scene
from characters.player import Player  # make sure you have this class

class World(Scene):
    player = Player()
    def __init__(self):
        super().__init__()
        self.player = Player([400, 300], "assets/player1.png")  # your image
        self.all_sprites = pygame.sprite.Group(self.player)

    def update(self, dt, keys):
        self.all_sprites.update(dt, keys)

    def draw(self, screen):
        screen.fill("black")
        self.all_sprites.draw(screen)
