#Main import block
#All Sorce code and article: https://github.com/vedantgoswami/SnakeGameAI/blob/main/model.py
# https://www.geeksforgeeks.org/ai-driven-snake-game-using-deep-q-learning/
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import os
import numpy as np

class Linear_QNet(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super().__init__()
        self.linear1 = nn.Linear(input_size, hidden_size)
        self.linear2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        x = F.relu(self.linear1(x))
        x = self.linear2(x)
        return x
    
    def save(self, file_name='model_name.pth'):
        model_folder_path = 'Path'
        file_name = os.path.join(model_folder_path, file_name)
        torch.save(self.state_dict(), file_name)

def get_state(self, game):
    head = game.snake[0]
    head = game.snake[0]
    point_l = Point(head.x - BLOCK_SIZE, head.y)
    point_r = Point(head.x + BLOCK_SIZE, head.y)
    point_u = Point(head.x, head.y - BLOCK_SIZE)
    point_d = Point(head.x, head.y + BLOCK_SIZE)
 
    dir_l = game.direction == Direction.LEFT
    dir_r = game.direction == Direction.RIGHT
    dir_u = game.direction == Direction.UP
    dir_d = game.direction == Direction.DOWN

    state = [
        # Danger Straight
        (dir_u and game.is_collision(point_u))or
        (dir_d and game.is_collision(point_d))or
        (dir_l and game.is_collision(point_l))or
        (dir_r and game.is_collision(point_r)),
 
        # Danger right
        (dir_u and game.is_collision(point_r))or
        (dir_d and game.is_collision(point_l))or
        (dir_u and game.is_collision(point_u))or
        (dir_d and game.is_collision(point_d)),
 
        # Danger Left
        (dir_u and game.is_collision(point_r))or
        (dir_d and game.is_collision(point_l))or
        (dir_r and game.is_collision(point_u))or
        (dir_l and game.is_collision(point_d)),
 
        # Move Direction
        dir_l,
        dir_r,
        dir_u,
        dir_d,
 
        # Food Location
        game.food.x < game.head.x,  # food is in left
        game.food.x > game.head.x,  # food is in right
        game.food.y < game.head.y,  # food is up
        game.food.y > game.head.y  # food is down
    ]
    return np.array(state, dtype=int)
    