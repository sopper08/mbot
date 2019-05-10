#!/usr/bin/env python3
# ros
import rospy
from mbot_movement_control_qt.msg import speeds_msg
from std_msgs.msg import Float64

# others
import ipdb
import argparse
import logging
import sys
from box import Box

class movement:
    def __init__(self, max_speed=10):
        self.right_speed = 0
        self.left_speed = 0
        self.max_speed = max_speed
    
    def update_speeds(self, left_speed_value, right_speed_value):
        self.left_speed = left_speed_value/self.max_speed
        self.right_speed = right_speed_value/self.max_speed

def pub_speeds_to_mbot(object):
    # TOPICS:
    #   *. /mbot/left_position_controller/command
    #   *. /mbot/right_position_controller/command
    pub_of_left = rospy.Publisher(name='/mbot/left_position_controller/command',
                                  data_class=Float64, queue_size=1)
    pub_of_left.publish(object.left_speed)
    pub_of_right = rospy.Publisher(name='/mbot/right_position_controller/command',
                                  data_class=Float64, queue_size=1)
    pub_of_right.publish(object.right_speed)

def callback(msg):
    # Update object:move right_speed & left_speed
    move.update_speeds(msg.speed_of_left_motor, msg.speed_of_right_motor)
    # Pub. speeds to mbot
    pub_speeds_to_mbot(move)


def subscriber(kwargs):
    rospy.Subscriber(data_class = speeds_msg, 
                     callback = callback,
                     **kwargs)
    rospy.spin()

def main(kwargs):
    # CONFIG
    cfg = Box.from_yaml(filename=kwargs.config_path)

    # GLOBAL VARS
    global move
    move = movement(**cfg.movement)

    # Pub. setting
    

    rospy.init_node(**cfg.rospy_init)
    subscriber(cfg.rospy_subscriber)

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