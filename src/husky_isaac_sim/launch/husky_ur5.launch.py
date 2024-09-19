import os
import yaml
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import Command, FindExecutable, PathJoinSubstitution, LaunchConfiguration
from launch_ros.substitutions import FindPackageShare
import launch_ros.descriptions

def generate_launch_description():
    robot_description=[{'robot_description': 
                 launch_ros.descriptions.ParameterValue( 
                    Command(
                        ['xacro ', "/home/husky_ur5_ws/src/husky_isaac_sim/urdf/husky_ur5.urdf.xacro"]),
                  value_type=str)  }]
    
    # robot_description_content = Command(
    #     [
    #         PathJoinSubstitution([FindExecutable(name="xacro")]),
    #         " ",
    #         PathJoinSubstitution(
    #             [FindPackageShare("husky_isaac_sim"), "urdf", "husky_ur5.urdf.xacro"]),
    #     ]
    # )
    # robot_description = {"robot_description": robot_description_content}
    robot_state_publisher_node = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        output="both",
        parameters=robot_description,
    )

    joint_state_publisher_node = Node(
        package="joint_state_publisher_gui",
        executable="joint_state_publisher_gui",
    )

    rviz_config_file = PathJoinSubstitution(
        [FindPackageShare("husky_isaac_sim"), "rviz", "husky_ur5.rviz"]
    )

    rviz_node = Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2",
        output={'both': 'log'},
        arguments=["-d", rviz_config_file],
    )

    # ur5_traj_server = Node(
    #     package='ur5_isaac_simulation',
    #     name='ur5_controller',
    #     executable='ur5_controller'
    # )

    # gripper_traj_server = Node(
    #     package='ur5_isaac_simulation',
    #     name='gripper_controller',
    #     executable='gripper_controller'
    # )

    nodes_to_start = [
        # ur5_traj_server,
        # gripper_traj_server,
        joint_state_publisher_node,
        robot_state_publisher_node,
        rviz_node
    ]
    return LaunchDescription(nodes_to_start)
