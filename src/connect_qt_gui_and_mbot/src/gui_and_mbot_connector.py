#!/usr/bin/env python3
# ros
import rospy
from geometry_msgs.msg import Twist

# others
import ipdb
import argparse
import logging
import sys
from box import Box

def update_speeds(speed_ratio):
    speeds = Twist()
    speed_ratio = float(speed_ratio)
    speeds.linear.x = float(rospy.get_param('speeds_linear_x'))/speed_ratio
    speeds.angular.z = float(rospy.get_param('speeds_angular_z'))/speed_ratio
    return speeds

def publisher(kwargs):
    # rate
    rate = rospy.Rate(kwargs.rate)
    # pub
    pub = rospy.Publisher(name=kwargs.name,
                          queue_size=kwargs.queue_size,
                          data_class=Twist)
    while not rospy.is_shutdown():
        speeds = update_speeds(kwargs.speed_ratio)
        pub.publish(speeds)
        rate.sleep()

def main(kwargs):
    # CONFIG
    cfg = Box.from_yaml(filename=kwargs.config_path)
    rospy.init_node(**cfg.rospy_init)
    publisher(cfg.rospy_Publisher)

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('config_path', type=str)
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s | %(levelname)s | %(name)s: %(message)s',
        level=logging.INFO, datefmt='%m-%d %H:%M:%S'
    )
    with ipdb.launch_ipdb_on_exception():
        sys.breakpointhook = ipdb.set_trace
        kwargs = parse_args()
        main(kwargs)