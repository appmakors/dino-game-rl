from game.game_config import BASE_GAME_SPEED, GROUND_LEVEL

class Obstacle:
    def __init__(self, image, x):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = GROUND_LEVEL - self.image.get_height()

    def update(self, game_speed=BASE_GAME_SPEED):
        self.rect.x -= game_speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def is_off_screen(self):
        return self.rect.right < 0
