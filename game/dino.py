from game.game_config import GRAVITY, JUMP_VELOCITY, GROUND_LEVEL

class Dino:
    def __init__(self, x, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = GROUND_LEVEL - self.image.get_height()
        self.is_jumping = False
        self.velocity = 0

    def update(self):
        if self.is_jumping:
            self.velocity += GRAVITY
            self.rect.y += self.velocity
            if self.rect.y >= GROUND_LEVEL - self.image.get_height():
                self.rect.y = GROUND_LEVEL - self.image.get_height()
                self.velocity = 0
                self.is_jumping = False

    def jump(self):
        if not self.is_jumping:
            self.is_jumping = True
            self.velocity = JUMP_VELOCITY

    def draw(self, screen):
        screen.blit(self.image, self.rect)
