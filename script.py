# Main import block
from logging import raiseExceptions
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

# Secondary Vars
global fruit_position
fruit_position = [random.randrange(1, (window_x//10)) * 10,
                  random.randrange(1, (window_y//10)) * 10]

# Initialize pygame

pygame.init()

# Initialize game window
pygame.display.set_caption("AI Snake")
#         #FPS Controller and counter
#         
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
def show_score(choice, color, font, size, game_window):

    # Creat the font
    score_font = pygame.font.SysFont(font, size)

    # Display for the surface object
    score_surface = score_font.render('Score: ' + str(score), True, color)

    # Create a rectanglear object for the score
    score_rect = score_surface.get_rect()

    # Displaying text
    screen.blit(score_surface, score_rect)

# Game over function

def game_over(game_window):
    global screen
    # Create the font
    my_font = pygame.font.SysFont('times new roman', 50)

    # Creating the text
    game_over_surface = my_font.render('Game Over -Your Score is : ' + str(score), True, red)

    # Creating the render object
    game_over_rect = game_over_surface.get_rect()

    # blit will draw text on screen
    screen.blit(game_over_surface, game_over_rect)

    
    # over_text = pygame.font.SysFont('times new roman', 100)
    # text = over_text.render("Game Over, your score is : " + str(score), True, red)
    # screen.blit(over_text, text)

# The main function
pygame.init()

def main():
    global screen
    screen = pygame.display.set_mode((window_x, window_y))
    screen.fill(black)
# Main Function
    while True:
        global change_to,direction,fruit_position,fruit,fruit_spawn, score, snake_position
        
        # handling key events
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                raise Exception("Game quit by user")
                exit(-1)
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
        screen.fill(black)
        
        for pos in snake_body:
            pygame.draw.rect(screen, green,
                            pygame.Rect(pos[0], pos[1], 10, 10))
        pygame.draw.rect(screen, white, pygame.Rect(
            fruit_position[0], fruit_position[1], 10, 10))
    
        # Game Over conditions
        while snake_position[0] < 0 or snake_position[0] > window_x-10:
            game_over(screen)
            pygame.display.update()
            pygame.time.delay(5000)
            # screen.fill(black)
            score = 0
            snake_position = [100, 50]
            change_to  = 'RIGHT'
            break
            
            
        while snake_position[1] < 0 or snake_position[1] > window_y-10:
            game_over(screen)
            pygame.display.update()
            pygame.time.delay(5000)
            # screen.fill(black)
            score = 0
            snake_position = [100, 50]
            change_to  = 'RIGHT'
            break
           
    
        # Touching the snake body
        for block in snake_body[1:]:
            if snake_position[0] == block[0] and snake_position[1] == block[1]:
                game_over(screen)
                pygame.display.update()
                pygame.time.delay(10000)
                # screen.fill(black)
                score = 0
                snake_position = [100, 50]
                change_to  = 'RIGHT'
                break
                
        # displaying score countinuously
        show_score(1, white, 'times new roman', 20, screen)
    
        # Refresh game screen
        pygame.display.update()
    
        # Frame Per Second /Refresh Rate
        fps.tick(snake_speed)
main()