#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'i am node 3 and i heard from topic 2 :  %s', data.data)

def listener():

    rospy.init_node('node3', anonymous=True)

    rospy.Subscriber('topic2', String, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()
