#!/usr/bin/env python

# ROS
import rospy
from gazebo_msgs.msg import ModelStates
from geometry_msgs.msg import Point

def callback(data):
    publisher = rospy.Publisher('/mbot/visual_Pos', Point, queue_size=10)

    point = Point()
    point.x = 5-data.pose[2].position.x
    point.y = 2.3-data.pose[2].position.y
    point.z = 0
    print(point.x)
    print(point.y)
    publisher.publish(point)
    

def main():
    rospy.init_node('update_pos_to_rosParam')
    rospy.sleep(2)
    rospy.Subscriber('/gazebo/model_states', ModelStates, callback)
    rospy.spin()


if __name__ == "__main__":
    main()