import pygame
from scenes.world import World

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

world = World()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    world.update(dt, keys)
    world.draw(screen)

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
