#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

print("give direction for x enter 1 for y enter 2, give direction 0 to quit")

direct = 1

def move():

    while(direct!=0):
        
         global direct
         direct=input("direction:  ")



         if(direct==1):

            rospy.init_node('robot_cleaner', anonymous=True)
            velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
            vel_msg = Twist()

            print("Let's move your robot")
            speed = input("Input your speed:")
            distance = input("Type your distance:")
            isForward = input("Foward?(backwars=0,everything else=forward): ")
    
            if(isForward):
                vel_msg.linear.x = abs(speed)
            else:
                vel_msg.linear.x = -abs(speed)
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = 0
    
            while not rospy.is_shutdown():

                t0 = rospy.Time.now().to_sec()
                current_distance = 0

                while(current_distance < distance):
                    
                    velocity_publisher.publish(vel_msg)
                    t1=rospy.Time.now().to_sec()
                    current_distance= speed*(t1-t0)

                vel_msg.linear.x = 0
                velocity_publisher.publish(vel_msg)
                break 

        
         elif(direct==2):

            rospy.init_node('robot_cleaner', anonymous=True)
            velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
            vel_msg = Twist()

            print("Let's move your robot")
            speed = input("Input your speed:")
            distance = input("Type your distance:")
            isForward = input("Foward?: ")#True or False
    
            if(isForward):
                vel_msg.linear.y = abs(speed)
            else:
                vel_msg.linear.y = -abs(speed)
            vel_msg.linear.x = 0
            vel_msg.linear.z = 0
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = 0
    
            while not rospy.is_shutdown():

                t0 = rospy.Time.now().to_sec()
                current_distance = 0

                while(current_distance < distance):
                    
                    velocity_publisher.publish(vel_msg)
                    t1=rospy.Time.now().to_sec()
                    current_distance= speed*(t1-t0)

                vel_msg.linear.y = 0
                velocity_publisher.publish(vel_msg)



if __name__ == '__main__':
     try:
         #Testing our function
         move()
     except rospy.ROSInterruptException: pass