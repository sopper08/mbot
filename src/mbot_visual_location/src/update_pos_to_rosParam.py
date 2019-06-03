#!/usr/bin/env python

# ROS
import rospy
from gazebo_msgs.msg import ModelStates

def callback(data):
    model_real_X = 5-data.pose[2].position.x
    model_real_Y = 2.3-data.pose[2].position.y
    rospy.set_param('model_real_X', model_real_X)
    rospy.set_param('model_real_Y', model_real_Y)

def main():
    rospy.init_node('update_pos_to_rosParam')
    rospy.Subscriber('/gazebo/model_states', ModelStates, callback)
    rospy.spin()


if __name__ == "__main__":
    main()