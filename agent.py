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
    
    def get_action(self, state):
        # random moves, tradeoff exploitation
        self.epsilon = 80 - self.n_game
        final_move = [0, 0, 0]
        if(random.randint(0, 200) < self.epsilon):
            move = random.randint(0, 2)
            final_move[move]
        else:
            state0 = torch.tensor(state, dtype=torch.float).cuda()
            prediction =    self.model(state0).cuda()
            move = torch.argmax(prediction).item()
            final_move[move] = 1
        return final_move
    
    def train_short_memory(self, state, action, reward, next_state, done):
        self.trainer.train_step(state, action, reward, next_state, done)
    
    def train_long_memory(self):
        if(len(self.memory) > BATCH_SIZE):
            mini_sample = random.sample(self.memory, BATCH_SIZE)
        else:
            mini_sample = self.memory
        states, actions, rewards, next_states, dones = zip(*mini_sample)
        self.trainer.train_step(states, actions, rewards, next_states, dones)
        self.model.load_state_dict(torch.load('PATH'))