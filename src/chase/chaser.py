#! /usr/bin/python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import sqrt

class Tom:
    def initialize(self):
        self.speed = rospy.get_param('chaser_speed_param')
        self.victim_position = Pose()
        self.position = Pose()

        self.pub = rospy.Publisher('/tom/cmd_vel', Twist, queue_size=10)
        rospy.init_node('0-Neil')
        rospy.Subscriber('/turtle1/pose', Pose, self.callback_victim_position)
        rospy.Subscriber('/tom/pose', Pose, self.callback_self_position)
        rospy.spin()

    def callback_self_position(self, msg):
        self.position = msg
        length = sqrt(pow(self.victim_position.x - self.position.x, 2) + pow(self.victim_position.y - self.position.y, 2))
        send_msg = Twist()
        x_dir = (self.victim_position.x - self.position.x) / length * self.speed
        y_dir = (self.victim_position.y - self.position.y) / length * self.speed
        send_msg.linear.x = x_dir
        send_msg.linear.y = y_dir
        self.pub.publish(send_msg)

    def callback_victim_position(self, msg):
        self.victim_position = msg

tom = Tom()
tom.initialize()