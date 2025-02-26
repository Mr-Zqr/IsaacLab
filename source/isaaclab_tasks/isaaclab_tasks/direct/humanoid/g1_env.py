# Copyright (c) 2022-2025, The Isaac Lab Project Developers.
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

from __future__ import annotations

from isaaclab_assets import HUMANOID_CFG
from isaaclab_assets import G1_CFG

import isaaclab.sim as sim_utils
from isaaclab.assets import ArticulationCfg
from isaaclab.envs import DirectRLEnvCfg
from isaaclab.scene import InteractiveSceneCfg
from isaaclab.sim import SimulationCfg
from isaaclab.terrains import TerrainImporterCfg, TerrainGeneratorCfg
from isaaclab.terrains.height_field.hf_terrains_cfg import HfWaveTerrainCfg
from isaaclab.utils import configclass

from isaaclab_tasks.direct.locomotion.locomotion_env import LocomotionEnv

@configclass
class G1EnvCfg(DirectRLEnvCfg):
    # env
    episode_length_s = 15.0
    decimation = 2
    action_scale = 1.0
    action_space = 37
    observation_space = 123
    state_space = 0

    # simulation
    sim: SimulationCfg = SimulationCfg(dt=1 / 120, render_interval=decimation)
    terrain = TerrainImporterCfg(
        prim_path="/World/ground",
        terrain_type="plane",
        collision_group=-1,
        physics_material=sim_utils.RigidBodyMaterialCfg(
            friction_combine_mode="average",
            restitution_combine_mode="average",
            static_friction=1.0,
            dynamic_friction=1.0,
            restitution=0.0,
        ),
        debug_vis=False,
    )

    # wave_terrain_cfg = HfWaveTerrainCfg(
    #     proportion = 1.0, 
    #     size = (20.0, 20.0),
    #     amplitude_range=(0.1, 0.5),
    #     num_waves=5,
    #     border_width=0.0,
    #     horizontal_scale=0.1,
    #     vertical_scale=0.005,
    #     slope_threshold=0.75,
    # )

    # terrain_generator_cfg = TerrainGeneratorCfg(
    #     seed=42,  # 随机种子，确保结果可复现
    #     curriculum=False,  # 不使用难度模式
    #     size=(20.0, 20.0),  # 每个子地形的尺寸
    #     border_width=0.5,  # 边框宽度
    #     border_height=1.0,  # 边框高度
    #     num_rows=12,  # 生成12行子地形
    #     num_cols=12,  # 生成12列子地形
    #     color_scheme="none",  # 不使用颜色方案
    #     horizontal_scale=0.1,  # 水平尺度
    #     vertical_scale=0.005,  # 垂直尺度
    #     slope_threshold=0.75,  # 坡度阈值
    #     sub_terrains={"wave": wave_terrain_cfg},  # 使用波浪地形配置
    #     difficulty_range=(0.0, 1.0),  # 难度范围
    #     use_cache=False,  # 不使用缓存
    #     cache_dir="/tmp/isaaclab/terrains",  # 缓存目录
    # )

    # terrain = TerrainImporterCfg(
    #     prim_path="/World/ground",
    #     terrain_type="generator",  # 修改为 wave 类型地形
    #     collision_group=-1,
    #     physics_material=sim_utils.RigidBodyMaterialCfg(
    #         friction_combine_mode="average",
    #         restitution_combine_mode="average",
    #         static_friction=1.0,
    #         dynamic_friction=1.0,
    #         restitution=0.0,
    #     ),
    #     debug_vis=False,
    #     terrain_generator= terrain_generator_cfg
    # )

    # scene
    scene: InteractiveSceneCfg = InteractiveSceneCfg(num_envs=4096, env_spacing=4.0, replicate_physics=True)

    # robot
    robot: ArticulationCfg = G1_CFG.replace(prim_path="/World/envs/env_.*/Robot")
    joint_gears: list = [
        50.0,  # left_hip_yaw
        50.0,  # right_hip_yaw
        50.0,  # torso
        50.0,  # left_hip_roll
        50.0,  # right_hip_roll
        50.0,  # left_shoulder_pitch
        50.0,  # right_shoulder_pitch
        50.0,  # left_hip_pitch
        50.0,  # right_hip_pitch
        50.0,  # left_shoulder_roll
        50.0,  # right_shoulder_roll
        50.0,  # left_knee
        50.0,  # right_knee
        50.0,  # left_shoulder_yaw
        50.0,  # right_shoulder_yaw
        50.0,  # left_ankle
        50.0,  # right_ankle
        50.0,  # left_elbow
        50.0,  # right_elbow
        50.0,  # left_hip_yaw
        50.0,  # right_hip_yaw
        50.0,  # torso
        50.0,  # left_hip_roll
        50.0,  # right_hip_roll
        50.0,  # left_shoulder_pitch
        50.0,  # right_shoulder_pitch
        50.0,  # left_hip_pitch
        50.0,  # right_hip_pitch
        50.0,  # left_shoulder_roll
        50.0,  # right_shoulder_roll
        50.0,  # left_knee
        50.0,  # right_knee
        50.0,  # left_shoulder_yaw
        50.0,  # right_shoulder_yaw
        50.0,  # left_ankle
        50.0,  # right_ankle
        50.0,  # left_elbow
    ]

    heading_weight: float = 0.7
    up_weight: float = 0.2

    energy_cost_scale: float = 0.01
    actions_cost_scale: float = 0.005
    alive_reward_scale: float = 3.0
    dof_vel_scale: float = 0.2

    death_cost: float = -0.5
    termination_height: float = 0.6

    angular_velocity_scale: float = 0.1
    contact_force_scale: float = 0.05


class G1Env(LocomotionEnv):
    cfg: G1EnvCfg

    def __init__(self, cfg: G1EnvCfg, render_mode: str | None = None, **kwargs):
        super().__init__(cfg, render_mode, **kwargs)
