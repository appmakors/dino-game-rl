import pygame
import sys
import random
from game.dino import Dino
from game.obstacle import Obstacle
from game.game_config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, BASE_GAME_SPEED, INCREASE_SPEED_AFTER, GROUND_LEVEL

# Toggle this to False when training your RL agent
render_mode = True

pygame.init()
screen = None
if render_mode:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

bg_color = (255, 255, 255)
dinojumping_img = pygame.image.load("assets/dino.png")
if render_mode:
    dinojumping_img = dinojumping_img.convert_alpha()

# Load obstacle assets
cactus_imgs = []
for i in range(1, 7):
    img = pygame.image.load(f"assets/cacti/cactus{i}.png")
    if render_mode:
        img = img.convert_alpha()
    cactus_imgs.append(img)

# Load ground image
ground_img = pygame.image.load("assets/ground.png")
if render_mode:
    ground_img = ground_img.convert_alpha()
ground_x1 = 0
ground_x2 = ground_img.get_width()
ground_y = GROUND_LEVEL - ground_img.get_height() / 2

# ptero_imgs = [
#     pygame.image.load("assets/ptero1.png").convert_alpha(),
#     pygame.image.load("assets/ptero2.png").convert_alpha()
# ]

# Create objects
dino = Dino(50, dinojumping_img)
obstacles = []
obstacle_timer = 0
score = 0

# Game loop
running = True
game_speed = BASE_GAME_SPEED
obstacle_timer_random = random.randint(90, 180)
while running:
    if render_mode:
        screen.fill(bg_color)
    dt = clock.tick(FPS) if render_mode else 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            dino.jump()

    # Increase game speed over time
    if score % INCREASE_SPEED_AFTER == 0 and score != 0:
        game_speed = BASE_GAME_SPEED + score // INCREASE_SPEED_AFTER

    dino.update()

    # Spawn new obstacles
    if obstacle_timer > obstacle_timer_random:
        obs_type = random.randint(0, 5)
        obstacles.append(Obstacle(cactus_imgs[obs_type], SCREEN_WIDTH))
        obstacle_timer = 0
        obstacle_timer_random = random.randint(90, 180)
    else:
        obstacle_timer += 1

    # Update and check obstacles
    for obs in obstacles[:]:
        obs.update(game_speed)
        if obs.is_off_screen():
            obstacles.remove(obs)
            score += 1
        if dino.rect.colliderect(obs.rect):
            print("Game Over")
            if render_mode:
                pygame.quit()
                sys.exit()
            else:
                running = False

    # Draw everything if in render mode
    if render_mode:
        dino.draw(screen)
        for obs in obstacles:
            obs.draw(screen)

        # Draw score
        font = pygame.font.Font("assets/PressStart2P-Regular.ttf", 20)
        score_surface = font.render(f"Score: {score}", True, (0, 0, 0))
        screen.blit(score_surface, (10, 10))


        # Draw and scroll the ground
        ground_x1 -= game_speed
        ground_x2 -= game_speed

        if ground_x1 + ground_img.get_width() < 0:
            ground_x1 = ground_x2 + ground_img.get_width()
        if ground_x2 + ground_img.get_width() < 0:
            ground_x2 = ground_x1 + ground_img.get_width()

        screen.blit(ground_img, (ground_x1, ground_y))
        screen.blit(ground_img, (ground_x2, ground_y))

        pygame.display.update()