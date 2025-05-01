import pygame
import sys
from game.dino import Dino
from game.obstacle import Obstacle
from game.game_config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# Load assets
dino_img = pygame.image.load("assets/DinoJumping.png").convert_alpha()
cactus_img = pygame.image.load("assets/cacti/cactus6.png").convert_alpha()
bg_color = (255, 255, 255)

# Create objects
dino = Dino(50, 220, dino_img)
obstacles = []
obstacle_timer = 0
score = 0

# Game loop
running = True
while running:
    screen.fill(bg_color)
    dt = clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            dino.jump()

    # Update
    dino.update()
    if obstacle_timer > 90:
        obstacles.append(Obstacle(cactus_img, SCREEN_WIDTH))
        obstacle_timer = 0
    else:
        obstacle_timer += 1

    for obs in obstacles[:]:
        obs.update()
        if obs.is_off_screen():
            obstacles.remove(obs)
            score += 1
        if dino.rect.colliderect(obs.rect):
            print("Game Over")
            pygame.quit()
            sys.exit()

    # Draw
    dino.draw(screen)
    for obs in obstacles:
        obs.draw(screen)

    # Score display
    font = pygame.font.SysFont(None, 30)
    score_surface = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_surface, (10, 10))

    pygame.display.update()
