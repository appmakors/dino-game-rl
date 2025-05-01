import pygame
import sys
import random
from game.dino import Dino
from game.obstacle import Obstacle
from game.game_config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, BASE_GAME_SPEED

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

bg_color = (255, 255, 255)
dinojumping_img = pygame.image.load("assets/dino.png").convert_alpha()
# Load obstacle assets
cactus_imgs = [
    pygame.image.load("assets/cacti/cactus1.png").convert_alpha(),
    pygame.image.load("assets/cacti/cactus2.png").convert_alpha(),
    pygame.image.load("assets/cacti/cactus3.png").convert_alpha(),
    pygame.image.load("assets/cacti/cactus4.png").convert_alpha(),
    pygame.image.load("assets/cacti/cactus5.png").convert_alpha(),
    pygame.image.load("assets/cacti/cactus6.png").convert_alpha()
]
# ptero_imgs = [
#     pygame.image.load("assets/ptero1.png").convert_alpha(),
#     pygame.image.load("assets/ptero2.png").convert_alpha()
# ]

# Create objects
dino = Dino(50, 205, dinojumping_img)
obstacles = []
obstacle_timer = 0
score = 0

# Game loop
running = True
game_speed = BASE_GAME_SPEED
obstacle_timer_random = random.randint(90, 180)
while running:
    screen.fill(bg_color)
    dt = clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            dino.jump()

    # Increase the game speed every 10 scores
    if score % 10 == 0 and score != 0:
        game_speed = BASE_GAME_SPEED + score // 10

    # Update
    dino.update()
    
    # Generate the obstacle randomly
    if obstacle_timer > obstacle_timer_random:
        obs_type = random.randint(0, 5)
        obstacles.append(Obstacle(cactus_imgs[obs_type], SCREEN_WIDTH))
        obstacle_timer = 0
        obstacle_timer_random = random.randint(90, 180)
    else:
        obstacle_timer += 1

    # Check if the obstacle is out of screen and dino collides with the obstacle
    for obs in obstacles[:]:
        obs.update(game_speed)
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
    font = pygame.font.Font("assets/PressStart2P-Regular.ttf", 20)
    score_surface = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_surface, (10, 10))

    pygame.display.update()
