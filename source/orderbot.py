#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

def chalai():
    pub = rospy.Publisher('/command',String,queue_size=1)
    rospy.init_node('CommandTaker',anonymous=True)
    r = rospy.Rate(1)
    rospy.loginfo("Taking commands...")
    while not rospy.is_shutdown():
        cmnd = input("Give command([forward,backward,left,right] [speed]): ")
        pub.publish(cmnd)
        r.sleep()
        


if __name__ == "__main__":
    try:
        chalai()
    except rospy.ROSInterruptException:
        pass
