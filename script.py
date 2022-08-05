# Main import block
from logging import raiseExceptions
import pygame
from time import sleep
import random
from state import GameState

pygame.init()

state = GameState()

# Initialize game window
pygame.display.set_caption("AI Snake")

# Display the score


def show_score(state, color, font, size):
    # Creat the font
    score_font = pygame.font.SysFont(font, size)

    # Display for the surface object
    score_surface = score_font.render(
        'Score: ' + str(state.score), True, color)

    # Create a rectanglear object for the score
    score_rect = score_surface.get_rect()

    # Displaying text
    state.screen.blit(score_surface, score_rect)

# Game over function


def game_over(state):
    state.dead = True
    state.should_tick = False

def refresh_display(state: GameState):
    state.screen.fill(state.black)

    # displaying score countinuously
    show_score(state, state.white, 'times new roman', 20)

    for pos in state.snake_body:
        pygame.draw.rect(state.screen, state.green,
                            pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(state.screen, state.red, pygame.Rect(
        state.apple_position[0], state.apple_position[1], 10, 10))
    
    if state.dead:
        # Create the font
        my_font = pygame.font.SysFont('times new roman', 50)

        # Creating the text
        game_over_surface = my_font.render(
            'Game Over -Your Score is : ' + str(state.score), True, state.red)

        # Creating the render object
        game_over_rect = game_over_surface.get_rect()

        # blit will draw text on screen
        state.screen.blit(game_over_surface, game_over_rect)

    # Refresh game screen
    pygame.display.update()

def main(state: GameState):
    state.screen = pygame.display.set_mode((state.window_x, state.window_y))
    state.screen.fill(state.black)

    # Main Function
    while True:
        # handling key events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise Exception("Game quit by user")
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    state.change_to = 'UP'
                if event.key == pygame.K_DOWN:
                    state.change_to = 'DOWN'
                if event.key == pygame.K_LEFT:
                    state.change_to = 'LEFT'
                if event.key == pygame.K_RIGHT:
                    state.change_to = 'RIGHT'
                if event.key == pygame.K_ESCAPE:
                    if state.dead:
                        state.reset()

        # If two keys pressed simultaneously
        # we don't want snake to move into two
        # directions simultaneously
        if state.change_to == 'UP' and state.direction != 'DOWN':
            state.direction = 'UP'
        if state.change_to == 'DOWN' and state.direction != 'UP':
            state.direction = 'DOWN'
        if state.change_to == 'LEFT' and state.direction != 'RIGHT':
            state.direction = 'LEFT'
        if state.change_to == 'RIGHT' and state.direction != 'LEFT':
            state.direction = 'RIGHT'
        
        
        # everything in here should be tick-only
        if state.should_tick:
            # Moving the snake
            if state.direction == 'UP':
                state.snake_position[1] -= 10
            if state.direction == 'DOWN':
                state.snake_position[1] += 10
            if state.direction == 'LEFT':
                state.snake_position[0] -= 10
            if state.direction == 'RIGHT':
                state.snake_position[0] += 10

            # Snake body growing mechanism
            # if fruits and snakes collide then scores
            # will be incremented by 10
            state.snake_body.insert(0, list(state.snake_position))
            if state.snake_position[0] == state.apple_position[0] and state.snake_position[1] == state.apple_position[1]:
                state.score += 10
                state.fruit_spawn = False
            else:
                state.snake_body.pop()

            if not state.fruit_spawn:
                state.apple_position = [random.randrange(1, (state.window_x//10)) * 10,
                                        random.randrange(1, (state.window_y//10)) * 10]

                state.fruit_spawn = True

        # Game Over conditions
        if state.snake_position[0] < 0 or state.snake_position[0] > state.window_x-10 \
                or state.snake_position[1] < 0 or state.snake_position[1] > state.window_y-10:
            game_over(state)

        # Touching the snake body
        for block in state.snake_body[1:]:
            if state.snake_position[0] == block[0] and state.snake_position[1] == block[1]:
                game_over(state)

        refresh_display(state)

        # Frame Per Second /Refresh Rate
        state.fps.tick(state.snake_speed)


main(state)
