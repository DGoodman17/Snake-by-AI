import pygame

import random


class GameState:
    def __init__(self):
        self.running = True

        # pressed keys
        self.pressed = pygame.key.get_pressed()

        # window dims
        self.window_x = 720
        self.window_y = 480

        # game config
        self.snake_speed = 15

        # define colours
        self.black = pygame.Color(0, 0, 0)
        self.white = pygame.Color(255, 255, 255)
        self.red = pygame.Color(255, 0, 0)
        self.green = pygame.Color(0, 255, 0)
        self.blue = pygame.Color(0, 0, 255)

        self.fruit_position = [random.randrange(1, (self.window_x//10)) * 10,
                               random.randrange(1, (self.window_y//10)) * 10]

        self.fps = pygame.time.Clock()

        # define snake location
        self.snake_position = [100, 50]
        self.snake_body = [
            [100, 50],
            [90, 50],
            [80, 50],
            [70, 50]
        ]

        # Apple positions
        self.apple_position = [random.randrange(1, (self.window_x//10)) * 10,
                               random.randrange(1, (self.window_y//10)) * 10]
        self.fruit_spawn = True

        # Setting the default direction
        self.direction = 'RIGHT'
        self.change_to  = self.direction

        # Initial score
        self.score = 0
