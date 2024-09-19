from omni.isaac.kit import SimulationApp

# simulation_app = SimulationApp({"headless": False})

from omni.isaac.core import World, SimulationContext
from omni.isaac.core.robots import Robot
from omni.isaac.core.utils import prims
from omni.isaac.manipulators import SingleManipulator
from omni.isaac.manipulators.grippers import ParallelGripper
from omni.isaac.core.utils.stage import add_reference_to_stage
from omni.isaac.core.utils.types import ArticulationAction
import numpy as np

my_world = World(stage_units_in_meters=1.0)
# simulation_context = SimulationContext(stage_units_in_meters=1.0)
my_world.scene.add_default_ground_plane()

#TODO: change this to your own path
asset_path = "/home/ubuntu/TJH/Work/omniverse/ur5_isaac_ws/src/ur5_isaac_simulation/usd/ur5_isaac_sim.usd"
add_reference_to_stage(usd_path=asset_path, prim_path="/World/Robots/ur5_robot")
# add_reference_to_stage(
#     "/home/ubuntu/TJH/Work/omniverse/usd/testbed_table2.usd", "/background"
# )
# prims.create_prim(
#     "/World/Robots/ur5_robot",
#     "Xform",
#     position=np.array([0.06, 0.06, 0.82]),
#     orientation=([1.0, 0.0, 0.0, 0.0]),
#     usd_path=asset_path
# )
# simulation_app.update()
articulated_system_1 = my_world.scene.add(Robot(prim_path="/World/Robots/ur5_robot", name="my_ur5"))

#define the gripper
# gripper = ParallelGripper(
#     #We chose the following values while inspecting the articulation
#     end_effector_prim_path="/World/Robots/ur5_robot/grasping_link",
#     joint_prim_names=["gripper_controller", "gripper_base_to_gripper_right3"],
#     joint_opened_positions=np.array([0, 0]),
#     joint_closed_positions=np.array([0.628, -0.628]),
#     action_deltas=np.array([-0.628, 0.628])
# )
# # #define the manipulator
# my_denso = my_world.scene.add(SingleManipulator(prim_path="/World/Robots", name="my_robot",
#                                                 end_effector_prim_name="gripper_link",
                                                # gripper=gripper))
#set the default positions of the other gripper joints to be opened so
#that its out of the way of the joints we want to control when gripping an object for instance.
# joints_default_positions = np.zeros(12)
# joints_default_positions[7] = 0.628
# joints_default_positions[8] = 0.628
# my_denso.set_joints_default_state(positions=joints_default_positions)
# my_world.scene.add_default_ground_plane()
# my_world.reset()
# simulation_context.initialize_physics()

# simulation_context.play()
# i = 0
# while simulation_app.is_running():
#     my_world.step(render=True)
#     # simulation_context.step(render=True)
#     # if my_world.is_playing():
#     #     if my_world.current_time_step_index == 0:
#     #         my_world.reset()
#     #     i += 1
#         # gripper_positions = my_denso.gripper.get_joint_positions()
#         # if i < 500:
#         #     #close the gripper slowly
#         #     my_denso.gripper.apply_action(
#         #         ArticulationAction(joint_positions=[gripper_positions[0] + 0.1, gripper_positions[1] - 0.1]))
#         # if i > 500:
#         #     #open the gripper slowly
#         #     my_denso.gripper.apply_action(
#         #         ArticulationAction(joint_positions=[gripper_positions[0] - 0.1, gripper_positions[1] + 0.1]))
#         # if i == 1000:
#         #     i = 0

# # simulation_context.stop()
# # my_world.close()
# simulation_app.close()
