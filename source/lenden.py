#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

class processCommand:
    def __init__(self) -> None:
        rospy.init_node('command_processer',anonymous=True)
        rospy.Subscriber('/command',String,self.clbk)
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

    def clbk(self,cmnd):
        rospy.loginfo('received command...')
        try:
            dir, speed = cmnd.data.split(" ")
            dir = dir.lower()
            speed = float(speed)/10
        except:
            dir,speed='',0
        vel = Twist()
        if dir=='forward':
            vel.linear.x = speed
        elif dir=='backward':
            vel.linear.x = -speed
        elif dir=='right':
            vel.angular.z = -speed
        elif dir=='left':
            vel.angular.z = speed
        else:
            vel.linear.x = 0
            vel.angular.z = 0
        self.pub.publish(vel)
        
        
if __name__=='__main__':
    node = processCommand()
    rospy.spin()