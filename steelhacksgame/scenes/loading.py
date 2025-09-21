import pygame
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from characters.player import Player
from scenes.scene import Scene

class Loading(Scene):
    def __init__(self):
        super().__init__()
        #initializing the chracter
       
    def update(self, dt, keys):
        pass

    #creates a black box
    def draw(self, screen):
        screen.fill(0,0,0)