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
        self.door_rect = pygame.Rect(130,150,120,175)
    
    #calls update so player can move around with the keys
    def update(self, dt, keys):
        self.all_sprites.update(dt, keys)
        if self.player.rect.colliderect(self.door_rect):
            print("Yayyyyyyy")

    #creates a black box
    def draw(self, screen):
        screen.blit(self.background, (0, 0))
        pygame.draw.rect(screen, (255, 0, 0), self.player.rect, 2)
        pygame.draw.rect(screen, (255,0,0), self.door_rect,2)
        self.all_sprites.draw(screen)

