from game.game_config import GRAVITY, JUMP_VELOCITY

class Dino:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.is_jumping = False
        self.velocity = 0

    def update(self):
        if self.is_jumping:
            self.velocity += GRAVITY
            self.rect.y += self.velocity

            if self.rect.y >= 220:  # ground level
                self.rect.y = 220
                self.velocity = 0
                self.is_jumping = False

    def jump(self):
        if not self.is_jumping:
            self.is_jumping = True
            self.velocity = JUMP_VELOCITY

    def draw(self, screen):
        screen.blit(self.image, self.rect)
