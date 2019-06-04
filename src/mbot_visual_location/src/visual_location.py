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
            trans_MtoB, rot_MtoB = tf_listener.lookupTransform('map', 'base_footprint', rospy.Time(0))
            model_real_pos = (rospy.get_param("model_real_X"),
                              rospy.get_param("model_real_Y"),
                              0)
            r_MtoB_real = np.dot(tf.transformations.translation_matrix(model_real_pos),  
                                tf.transformations.quaternion_matrix(rot_MtoB))

            trans_OtoB, rot_OtoB = tf_listener.lookupTransform('odom', 'base_footprint', rospy.Time(0))
            r_OtoB = np.dot(tf.transformations.translation_matrix(trans_OtoB),  
                            tf.transformations.quaternion_matrix(rot_OtoB))

            r_MtoO = np.dot(r_MtoB_real,
                            tf.transformations.inverse_matrix(r_OtoB))
            trans_MtoO = tf.transformations.translation_from_matrix(r_MtoO)
            rot_MtoO = tf.transformations.quaternion_from_matrix(r_MtoO)

            br = tf.TransformBroadcaster()
            br.sendTransform(trans_MtoO,
                            rot_MtoO,
                            rospy.Time.now(),
                            'odom',
                            'map')
            rospy.loginfo("visual!")

            trans_MtoB, rot_MtoB = tf_listener.lookupTransform('map', 'base_footprint', rospy.Time(0))
            # print(trans_MtoB)
            # print(model_real_pos)

            # rospy.sleep(0.1)
        
        
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            print("except")
            continue



if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass