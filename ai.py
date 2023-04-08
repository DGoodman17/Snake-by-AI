import script, state, reward
import gym

class custom_game(gym.Env):
    def __init__(self, grid_size=12):
        ...
        self.action_space = ... # Possible actions
        self.observation_space =... # Possible observations
    def _get_obs(self):
        """Calulates the observations (input) of current state"""
        ...
        return self.observation_space
    