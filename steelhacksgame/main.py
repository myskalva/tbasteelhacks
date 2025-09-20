import pygame
from scenes.bedroom import Bedroom



pygame.init()
screen = pygame.display.set_mode((720, 480))
#helps with making the frame rate consistent across computers
clock = pygame.time.Clock()
running = True
dt = 0


bedroom = Bedroom()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    bedroom.update(dt, keys)
    bedroom.draw(screen)

    pygame.display.flip()
    dt = clock.tick(60) / 1000
    


pygame.quit()
