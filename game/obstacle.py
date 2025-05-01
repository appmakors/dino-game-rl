from game.game_config import BASE_GAME_SPEED

class Obstacle:
    def __init__(self, image, x):
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, 230))

    def update(self, game_speed=BASE_GAME_SPEED):
        self.rect.x -= game_speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def is_off_screen(self):
        return self.rect.right < 0
