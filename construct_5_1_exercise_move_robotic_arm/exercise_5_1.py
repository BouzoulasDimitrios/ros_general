#! /usr/bin/env python

import rospy
# Import the service message used by the service /execute_trajectory
from trajectory_by_name_srv.srv import ExecTraj, ExecTrajRequest  
import sys

# Initialise a ROS node with the name service_client
rospy.init_node('service_client')

# Wait for the service client /execute_trajectory to be running
rospy.wait_for_service('/execute_trajectory') 

# Create the connection to the service
execute_trajectory_service = rospy.ServiceProxy('/execute_trajectory', ExecTraj)

# Create an object of type TrajByNameRequest
ExecTraj_object = ExecTrajRequest()

# Fill the variable ExecTraj_name of this object with the desired value
ExecTraj_object.ExecTraj = "release_food"

# Send through the connection the name of the trajectory to be executed by the robot
result = execute_trajectory_service(ExecTraj_object)

# Print the result given by the service called
print(result)


