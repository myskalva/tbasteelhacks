import pygame
class Player(pygame.sprite.Sprite):
    def __init__(self, pos, image_path="assets/player1.png"):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(center=pos)
        self.speed = 200
    def update(self, dt, keys):
        # move the player
        if keys[pygame.K_w]:
            self.rect.y -= self.speed * dt
        if keys[pygame.K_s]:
            self.rect.y += self.speed * dt
        if keys[pygame.K_a]:
            self.rect.x -= self.speed * dt
        if keys[pygame.K_d]:
            self.rect.x += self.speed * dt
        
        screen_rect = pygame.Rect(0, 0, 720, 480)
        self.rect = self.rect.clamp(screen_rect)
