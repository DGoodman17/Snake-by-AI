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
    global game_window
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
apple_position = [random.randrange(1, (window_x//10)) * 10,
                  random.randrange(1, (window_y//10)) * 10]
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

# Game over function

def game_over():
    
    # Create the font
    my_font = pygame.font.SysFont('times new roman', 50)

    # Creating the text
    game_over_surface = my_font.render('Your Score is : ' + str(score), True)

    # Creating the render object
    game_over_rect = game_over_surface.get_rect()

    # blit will draw text on screen
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

# The main function
pygame.init()
screen = pygame.display.set_mode((window_x, window_y))
def main():
# Main Function
    global change_to
    while True:
        screen.fill(black)
        
        
        # handling key events
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_to = 'UP'
                if event.key == pygame.K_DOWN:
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT:
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT:
                    change_to = 'RIGHT'
    
        # If two keys pressed simultaneously
        # we don't want snake to move into two
        # directions simultaneously
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'
    
        # Moving the snake
        if direction == 'UP':
            snake_position[1] -= 10
        if direction == 'DOWN':
            snake_position[1] += 10
        if direction == 'LEFT':
            snake_position[0] -= 10
        if direction == 'RIGHT':
            snake_position[0] += 10
    
        # Snake body growing mechanism
        # if fruits and snakes collide then scores
        # will be incremented by 10
        snake_body.insert(0, list(snake_position))
        if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
            score += 10
            fruit_spawn = False
        else:
            snake_body.pop()
            
        if not fruit_spawn:
            fruit_position = [random.randrange(1, (window_x//10)) * 10,
                            random.randrange(1, (window_y//10)) * 10]
            
        fruit_spawn = True
        game_window.fill(black)
        
        for pos in snake_body:
            pygame.draw.rect(game_window, green,
                            pygame.Rect(pos[0], pos[1], 10, 10))
        pygame.draw.rect(game_window, white, pygame.Rect(
            fruit_position[0], fruit_position[1], 10, 10))
    
        # Game Over conditions
        if snake_position[0] < 0 or snake_position[0] > window_x-10:
            game_over()
            main()
        if snake_position[1] < 0 or snake_position[1] > window_y-10:
            game_over()
            main()
    
        # Touching the snake body
        for block in snake_body[1:]:
            if snake_position[0] == block[0] and snake_position[1] == block[1]:
                game_over()
                main()
        # displaying score countinuously
        show_score(1, white, 'times new roman', 20)
    
        # Refresh game screen
        pygame.display.update()
    
        # Frame Per Second /Refresh Rate
        fps.tick(snake_speed)
main()