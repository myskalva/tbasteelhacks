import pygame
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from characters.player import Player
from scenes.scene import Scene

class Kitchen(Scene):
    def __init__(self):
        super().__init__()
        self.background = pygame.image.load("assets/kitchenBackground.gif").convert()
        self.background = pygame.transform.scale(self.background, (720, 480))
        #initializing the chracter
        self.player = Player([400, 300], "assets/player1.png")  # your image
        self.all_sprites = pygame.sprite.Group(self.player)
        self.return_rect = pygame.Rect(0,350,20,175)
        self.outside_rect = pygame.Rect(700,350,20,175)
        self.outside = False
        self.return_bed = False

    
    #calls update so player can move around with the keys
    def update(self, dt, keys):
        self.all_sprites.update(dt, keys)
        if self.player.rect.colliderect(self.return_rect):
            self.return_bed = True
        if self.player.rect.colliderect(self.outside_rect):
            self.outside = True
            

    #creates a black box
    def draw(self, screen):
        screen.blit(self.background, (0, 0))
        pygame.draw.rect(screen, (255, 0, 0), self.player.rect, 2)
        pygame.draw.rect(screen, (255,0,0), self.outside_rect,2)
        pygame.draw.rect(screen, (255,0,0), self.return_rect,2)
        self.all_sprites.draw(screen)
