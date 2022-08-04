# Main import block
import pygame
from time import sleep
import random


pygame.init()

# Vars
running = True


# Keyboard input variable
pressed = pygame.key.get_pressed()

snake_speed = 15

# Windows size
window_x = 720
window_y = 480

# Define colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Initialize pygame

pygame.init()

# Initialize game window
pygame.display.set_caption("AI Snake")
while running:
    game_window = pygame.display.set_mode((window_x, window_y))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        #FPS Controller and counter
        fps = pygame.time.Clock()

# Define the snake position
snake_position = [100, 50]

# Define the first four blocks of the snake
# Body
snake_body = [
    [100, 50],
    [90, 50],
    [80, 50],
    [70, 50]
]

# Apple positions
apple_position = [random.randrange(1, (window_x//10) * 10),
                    random.randrange(1, (window_y//10 * 10))]
fruit_spawn = True

# Setting the default direction
direction = 'RIGHT'
change_to  = direction

# Initial score
score = 0

# Display the score
def show_score(choice, color, font, size):

    # Creat the font
    score_font = pygame.SysFont(font, size)

    # Display for the surface object
    score_surface = score_font.render('Score: ' + str(score), True, color)

    # Create a rectanglear object for the score
    score_rect = score.surface.get_rect()

    # Displaying text
    game_window.blit(score_surface, score_rect)
