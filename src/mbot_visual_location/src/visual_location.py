#!/usr/bin/env python

# ROS
import rospy
import rosbag
import rospkg
import tf
import pdb
from gazebo_msgs.msg import ModelStates

position = []

def callback(data):
    print(data)

def main(): 
    rospy.init_node('visual_location')
    
    tf_listener = tf.TransformListener()

    while not rospy.is_shutdown():
        try:
            trans_map, rot_map = tf_listener.lookupTransform('map', 'base_footprint', rospy.Time(0))
            trans_odom, rot_odom = tf_listener.lookupTransform('odom', 'base_footprint', rospy.Time(0))
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            print("except")
            continue

        model_real_pos = [rospy.get_param("model_real_X"),
                          rospy.get_param("model_real_Y")]
        
        print(tf.transformations.euler_from_quaternion(rot_map))
        
        


        # br = tf.TransformBroadcaster()
        # br.sendTransform((trans[0], trans[1], trans[2]),
        #                  rot,
        #                  rospy.Time.now(),
        #                  'odom',
        #                  'map')

        rospy.sleep(1)
    
        


if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass