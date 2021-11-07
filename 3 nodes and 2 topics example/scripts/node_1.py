#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('topic1', String, queue_size=10)
    rospy.init_node('node1', anonymous=True)
    rate = rospy.Rate(1) # 10hz
    while not rospy.is_shutdown():
        node1_message = " node 1 publishing to topic 1" 
        rospy.loginfo(node1_message)
        pub.publish(node1_message)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
