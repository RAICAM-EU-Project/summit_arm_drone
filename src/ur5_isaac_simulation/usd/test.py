# Copyright (c) 2021-2023, NVIDIA CORPORATION. All rights reserved.
#
# NVIDIA CORPORATION and its licensors retain all intellectual property
# and proprietary rights in and to this software, related documentation
# and any modifications thereto. Any use, reproduction, disclosure or
# distribution of this software and related documentation without an express
# license agreement from NVIDIA CORPORATION is strictly prohibited.
#

from omni.isaac.kit import SimulationApp

simulation_app = SimulationApp({"headless": False})

import argparse
import sys

import carb
import numpy as np
from omni.isaac.core import World
from omni.isaac.core.robots import Robot
from omni.isaac.core.utils import prims, extensions
from omni.isaac.core.utils.nucleus import get_assets_root_path
from omni.isaac.core.utils.stage import add_reference_to_stage, get_stage_units
from omni.isaac.core.utils.types import ArticulationAction
from omni.isaac.cloner import Cloner
# parser = argparse.ArgumentParser()
# parser.add_argument("--test", default=False, action="store_true", help="Run in test mode")
# args, unknown = parser.parse_known_args()

# assets_root_path = get_assets_root_path()
# if assets_root_path is None:
#     carb.log_error("Could not find Isaac Sim assets folder")
#     simulation_app.close()
#     sys.exit()
extensions.enable_extension("ur5sim.ros2contactpublisher")

my_world = World(stage_units_in_meters=1.0)
my_world.scene.add_default_ground_plane()
asset_path = "/home/ur5_isaac_ws/src/ur5_isaac_simulation/usd/ur5_robot.usd"
# asset_path = "omniverse://localhost/ur3e_gripper_humble_moveit2-humble/ur3e.usd"
# asset_path = assets_root_path + "/Isaac/Robots/Franka/franka_alt_fingers.usd"
# Cloner.define_base_env(base_env_path="World/robot")
add_reference_to_stage(usd_path=asset_path, prim_path="/World/ur5_robot")
# prims.create_prim(
#     "/World"
#     "Xform",
#     position=np.array([0.06, 0.06, 0.82]),
#     orientation=([1.0, 0.0, 0.0, 0.0]),
#     usd_path=asset_path
# )

# add_reference_to_stage(usd_path=asset_path, prim_path="/World/Franka_2")
# articulated_system_1 = my_world.scene.add(Robot(prim_path="/World/ur3e", name="ur5"))
# articulated_system_2 = my_world.scene.add(Robot(prim_path="/World/Franka_2", name="my_franka_2"))
# my_world.reset()
simulation_app.update()
# for i in range(5):
#     print("resetting...")
#     my_world.reset()
#     articulated_system_1.set_world_pose(position=np.array([0.0, 2.0, 0.0]) / get_stage_units())
#     # articulated_system_2.set_world_pose(position=np.array([0.0, -2.0, 0.0]) / get_stage_units())
#     articulated_system_1.set_joint_positions(np.array([1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5]))
#     for j in range(500):
#         my_world.step(render=True)
#         # if j == 100:
#         #     articulated_system_2.get_articulation_controller().apply_action(
#         #         ArticulationAction(joint_positions=np.array([1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5]))
#         #     )
#         # if j == 400:
#         #     print("Franka 1's joint positions are: ", articulated_system_1.get_joint_positions())
#         #     print("Franka 2's joint positions are: ", articulated_system_2.get_joint_positions())
#     # if args.test is True:
#     #     break
while simulation_app.is_running():
    my_world.step(render=True)
simulation_app.close()