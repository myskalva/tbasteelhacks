import pygame
from scenes.world import World

pygame.init()
screen = pygame.display.set_mode((720, 480))
clock = pygame.time.Clock()
running = True
dt = 0

world = World()  # instantiate the world

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    world.update(dt, keys)       # update logic
    world.draw(screen)           # draw to screen

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
