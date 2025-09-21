import pygame
from scenes.kitchen import Kitchen
from scenes.bedroom import Bedroom
from scenes.loading import Loading



pygame.init()
screen = pygame.display.set_mode((720, 480))
#helps with making the frame rate consistent across computers
clock = pygame.time.Clock()
running = True
dt = 0


kitchen = Kitchen()
bedroom = Bedroom()
loading = Loading()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if bedroom.kitchen:
        kitchen.update(dt, keys)
        kitchen.draw(screen)
    
    
    if bedroom.bedroom or kitchen.return_bed:
        bedroom.update(dt, keys)
        bedroom.draw(screen)

    if kitchen.outside:
        loading.update(dt, keys)
        loading.draw(screen)



    




    pygame.display.flip()
    dt = clock.tick(60) / 1000
    


pygame.quit()
