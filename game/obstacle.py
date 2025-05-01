class Obstacle:
    def __init__(self, image, x):
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, 230))

    def update(self):
        self.rect.x -= 5

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def is_off_screen(self):
        return self.rect.right < 0
