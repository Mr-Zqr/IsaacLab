# Copyright (c) 2022-2025, The Isaac Lab Project Developers.
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

import gymnasium as gym

from . import agents
from .factory_nut_bolt_pick_env import FactoryNutBoltPickEnv
from .factory_nut_bolt_pick_env_cfg import FactoryNutBoltPickEnvCfg

##
# Register Gym environments.
##

# gym.register(
#     id="Isaac-Factory-NutThread-Direct-v0",
#     entry_point="isaaclab_tasks.direct.factory:FactoryEnv",
#     disable_env_checker=True,
#     kwargs={
#         "env_cfg_entry_point": FactoryTaskNutThreadCfg,
#         "rl_games_cfg_entry_point": f"{agents.__name__}:rl_games_ppo_cfg.yaml",
#     },
# )

gym.register(
    id="Factory-NBP-Direct",
    entry_point="isaaclab_tasks.direct.factory_nut_bolt_pick:FactoryNutBoltPickEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": FactoryNutBoltPickEnvCfg,
        "rl_games_cfg_entry_point": f"{agents.__name__}:rl_games_ppo_cfg_nutbolt_pick.yaml",
    },
)