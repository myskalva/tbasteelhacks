import pygame
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from characters.player import Player
from scenes.scene import Scene

class Bedroom(Scene):
    def __init__(self):
        super().__init__()
        self.background = pygame.image.load("assets/bedroom.png").convert()
        self.background = pygame.transform.scale(self.background, (720, 480))
        #initializing the chracter
        self.player = Player([400, 300], "assets/player1.png")  # your image
        self.all_sprites = pygame.sprite.Group(self.player)
    
    #calls update so player can move around with the keys
    def update(self, dt, keys):
        self.all_sprites.update(dt, keys)

    #creates a black box
    def draw(self, screen):
        screen.blit(self.background, (0, 0))
        self.all_sprites.draw(screen)
