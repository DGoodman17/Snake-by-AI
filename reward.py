# Main import block
import numpy as np
from state import GameState
from logging import raiseExceptions
import pygame

# Init visual screen for the game
pygame.init()

# Main var block
state = GameState()

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