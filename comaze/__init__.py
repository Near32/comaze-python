from .env import *
from .utils import *
from .agents import *

from gym.envs.registration import register

register(
    id='CoMaze-7x7-Sparse-v0',
    entry_point='comaze.env:CoMazeGymEnv7x7Sparse'
)