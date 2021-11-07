#!/usr/bin/env python

import rospy
from std_msgs.msg import String


def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'i am node 2 and i heard from topic 1 :  %s', data.data)

def listener():

    rospy.Subscriber('topic1', String, callback)
    pub = rospy.Publisher('topic2', String, queue_size=10)
    rospy.init_node('node2', anonymous=True)
    rate = rospy.Rate(1) # 10hz
    
    while not rospy.is_shutdown():
        node2_message = " node 2 publishing to topic 3 " 
        rospy.loginfo(node2_message)
        pub.publish(node2_message)
        rate.sleep()

    rospy.spin()

if __name__ == '__main__':
    listener()

