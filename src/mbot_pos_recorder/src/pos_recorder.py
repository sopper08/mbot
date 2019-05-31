#!/usr/bin/env python

# ROS
import rospy
import rosbag
import rospkg
import tf
import pdb
from gazebo_msgs.msg import ModelStates
import json

def get_datas(path):
    bag = rosbag.Bag(path)

    tf_transformer = tf.Transformer(True, rospy.Duration(3600.0))

    odom_pos = []
    for topic, msg, t in bag.read_messages(topics=['/tf']):
        for msg_tf in msg.transforms:
            tf_transformer.setTransform(msg_tf)
        try: 
            xy, _ = tf_transformer.lookupTransform('map', 'base_footprint', rospy.Time(0))
            odom_pos.append({'time': t.to_nsec(),
                            'x': xy[0],
                            'y': xy[1]})
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue
    
    real_pos = []
    for topic, msg, t in bag.read_messages(topics=['/gazebo/model_states']):
        # m = ModelStates()
        real_pos.append({'time': t.to_nsec(),
                         'x': msg.pose[2].position.x,
                         'y': msg.pose[2].position.y})
        
    bag.close()
    
    return odom_pos, real_pos


def main():
    rospack = rospkg.RosPack()
    pkg_path = rospack.get_path('mbot_pos_recorder')
    bag_path = pkg_path + '/bags/2019-05-30-11-57-54.bag'

    odom_pos, real_pos = get_datas(bag_path)

    with open(pkg_path+'/tmp_datas/odom_pos.json', 'w') as f:
        json.dump(odom_pos, f)
    
    with open(pkg_path+'/tmp_datas/real_pos.json', 'w') as f:
        json.dump(real_pos, f)

if __name__ == '__main__':
    main()