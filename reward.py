# Main import block
import numpy as np
from state import GameState
from logging import raiseExceptions
import pygame

# Init visual screen for the game
pygame.init()

# Main var block
state = GameState()
highscore = 0
score = state.score
initial_reward = 0
highest_reward = 0
current_reward = 0

#Main code block
class AiReward():
  def __init__(reward_value, reward_value_real):
    np.array(reward_value)
    np.array(reward_value_real)

    if state.snake_position[0] == state.apple_position[0] and state.snake_position[1] == state.apple_position[1]:
        reward_value[0] = 10
        reward_value_real[0] = 10
        raise Exception("AI Reward has gone up")
    elif state.snake_position[0] == state.apple_position[0] and state.snake_position[1]!= state.apple_position[1]:
      reward_value[0] = -10
      raise Exception("AI Reward has gone down")
if highscore < score:
    raise Exception("New highscore")
    highscore = score
    console.log("Hightscore was set to: " + str(highscore))
def check_reward_score(initial_reward, highest_reward):
    if initial_reward > highest_reward:
        raise Exception("New high on reward")
        highest_reward = current_reward
        console.log("Newest highscore on reward: " + str(highest_reward))
    elif initial_reward < highest_reward:
        raise Exception("No new high on reward")
        console.log("No new highscore on reward.")