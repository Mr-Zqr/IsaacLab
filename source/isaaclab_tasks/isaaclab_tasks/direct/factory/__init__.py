'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2025-02-07 13:02:19
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2025-02-21 13:01:32
FilePath: /Documents/IsaacLab/source/isaaclab_tasks/isaaclab_tasks/direct/factory/__init__.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
# Copyright (c) 2022-2025, The Isaac Lab Project Developers.
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

import gymnasium as gym

from . import agents
from .factory_env import FactoryEnv, FactoryEnvPick
from .factory_env_cfg import FactoryTaskGearMeshCfg, FactoryTaskNutThreadCfg, FactoryTaskPegInsertCfg, FactoryTaskNutBoltPickCfg

##
# Register Gym environments.
##

gym.register(
    id="Isaac-Factory-PegInsert-Direct-v0",
    entry_point="isaaclab_tasks.direct.factory:FactoryEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": FactoryTaskPegInsertCfg,
        "rl_games_cfg_entry_point": f"{agents.__name__}:rl_games_ppo_cfg.yaml",
    },
)

gym.register(
    id="Isaac-Factory-GearMesh-Direct-v0",
    entry_point="isaaclab_tasks.direct.factory:FactoryEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": FactoryTaskGearMeshCfg,
        "rl_games_cfg_entry_point": f"{agents.__name__}:rl_games_ppo_cfg.yaml",
    },
)

gym.register(
    id="Isaac-Factory-NutThread-Direct-v0",
    entry_point="isaaclab_tasks.direct.factory:FactoryEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": FactoryTaskNutThreadCfg,
        "rl_games_cfg_entry_point": f"{agents.__name__}:rl_games_ppo_cfg.yaml",
    },
)

gym.register(
    id="Isaac-Factory-NutBoltPick-Direct-v0",
    entry_point="isaaclab_tasks.direct.factory:FactoryEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": FactoryTaskNutBoltPickCfg,
        "rl_games_cfg_entry_point": f"{agents.__name__}:rl_games_ppo_cfg.yaml",
    },
    
)