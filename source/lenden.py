#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

class processCommand:
    def __init__(self) -> None:
        rospy.init_node('command_processer',anonymous=True)
        rospy.Subscriber('/command',String,self.clbk)
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.vel = Twist()

    def clbk(self,cmnd):
        rospy.loginfo('received command...')
        dir, speed = cmnd.data.split(" ")
        dir = dir.lower()
        speed = float(speed)/10
        if dir=='forward':
            self.vel.linear.x = speed
        elif dir=='backward':
            self.vel.linear.x = -speed
        elif dir=='right':
            self.vel.angular.z = -speed
        elif dir=='left':
            self.vel.angular.z = speed
        else:
            self.vel.linear.x = 0
            self.vel.angular.z = 0
        self.pub.publish(self.vel)
        
        
if __name__=='__main__':
    node = processCommand()
    rospy.spin()