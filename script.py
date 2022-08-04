import pygame
from time import sleep
import random



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
while True:
    game_window = pygame.display.set_mode((window_x, window_y))

    #FPS Controller and counter
    fps = pygame.time.Clock()

