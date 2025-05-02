from gym.envs.registration import register
from mjrl.envs.mujoco_env import MujocoEnv

# Swing the door open
register(
    id='door-v0',
    entry_point='mj_envs.hand_manipulation_suite:DoorEnvV0',
    max_episode_steps=200,
)
from mj_envs.hand_manipulation_suite.door_v0 import DoorEnvV0

# Swing the door open (Sparse)
register(
    id='door-v0_sparse',
    entry_point='mj_envs.hand_manipulation_suite:DoorEnvSparseV0',
    max_episode_steps=200,
)
from mj_envs.hand_manipulation_suite.door_v0 import DoorEnvSparseV0

# Hammer a nail into the board
register(
    id='hammer-v0',
    entry_point='mj_envs.hand_manipulation_suite:HammerEnvV0',
    max_episode_steps=200,
)
from mj_envs.hand_manipulation_suite.hammer_v0 import HammerEnvV0

# Hammer a nail into the board (Sparse)
register(
    id='hammer-v0_sparse',
    entry_point='mj_envs.hand_manipulation_suite:HammerEnvSparseV0',
    max_episode_steps=200,
)
from mj_envs.hand_manipulation_suite.hammer_v0 import HammerEnvSparseV0

# Reposition a pen in hand
register(
    id='pen-v0',
    entry_point='mj_envs.hand_manipulation_suite:PenEnvV0',
    max_episode_steps=100,
)
from mj_envs.hand_manipulation_suite.pen_v0 import PenEnvV0

# Reposition a pen in hand
register(
    id='pen-v0_sparse',
    entry_point='mj_envs.hand_manipulation_suite:PenEnvSparseV0',
    max_episode_steps=100,
)
from mj_envs.hand_manipulation_suite.pen_v0 import PenEnvSparseV0

# Relcoate an object to the target
register(
    id='relocate-v0',
    entry_point='mj_envs.hand_manipulation_suite:RelocateEnvV0',
    max_episode_steps=200,
)
from mj_envs.hand_manipulation_suite.relocate_v0 import RelocateEnvV0

# Relcoate an object to the target (Sparse)
register(
    id='relocate-v0_sparse',
    entry_point='mj_envs.hand_manipulation_suite:RelocateEnvSparseV0',
    max_episode_steps=200,
)
from mj_envs.hand_manipulation_suite.relocate_v0 import RelocateEnvSparseV0