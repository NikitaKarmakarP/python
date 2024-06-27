import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Ball Bounce Game')

# Ball settings
ball_size = 20
ball_speed = [3, 3]
ball_pos = [random.randint(ball_size, screen_width - ball_size),
            random.randint(ball_size, screen_height - ball_size)]

# Clock object to control the game's frame rate
clock = pygame.time.Clock()
fps = 60

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the ball
    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    # Ball collision with walls
    if ball_pos[0] <= ball_size or ball_pos[0] >= screen_width - ball_size:
        ball_speed[0] = -ball_speed[0]
    if ball_pos[1] <= ball_size or ball_pos[1] >= screen_height - ball_size:
        ball_speed[1] = -ball_speed[1]

    # Fill the screen with black
    screen.fill(black)

    # Draw the ball
    pygame.draw.circle(screen, red, ball_pos, ball_size)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(fps)

# Quit Pygame
pygame.quit()
