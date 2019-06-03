#!/usr/bin/env python

# ROS
import rospy
import rosbag
import rospkg
import tf
import pdb
from gazebo_msgs.msg import ModelStates

import numpy as np

def callback(data):
    print(data)

def main(): 
    rospy.init_node('visual_location')
    
    tf_listener = tf.TransformListener()

    while not rospy.is_shutdown():
        try:
            trans_map, rot_map = tf_listener.lookupTransform('visual_map', 'base_footprint', rospy.Time(0))
            trans_odom, rot_odom = tf_listener.lookupTransform('odom', 'base_footprint', rospy.Time(0))
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            print("except")
            continue

        model_real_pos = [rospy.get_param("model_real_X"),
                          rospy.get_param("model_real_Y")]
        
        trans_map[0] = model_real_pos[0]
        trans_map[1] = model_real_pos[1]

        trans_map_mat = tf.transformations.translation_matrix(trans_map)
        rot_map_mat = tf.transformations.quaternion_matrix(rot_map)
        r_map = np.dot(trans_map_mat, rot_map_mat)

        trans_odom_mat = tf.transformations.translation_matrix(trans_odom)
        rot_odom_mat = tf.transformations.quaternion_matrix(rot_odom)
        r_odom = np.dot(trans_odom_mat, rot_odom_mat)

        r_mo = np.dot(r_map, tf.transformations.inverse_matrix(r_odom))
        trans_mo = tf.transformations.translation_from_matrix(r_mo)
        rot_mo = tf.transformations.quaternion_from_matrix(r_mo)


        br = tf.TransformBroadcaster()
        br.sendTransform(trans_mo,
                         rot_mo,
                         rospy.Time.now(),
                         'odom',
                         'visual_map')
        rospy.loginfo("visual!")
        rospy.sleep(1)
    
        


if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass