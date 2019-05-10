#!/usr/bin/env python3
# ros
import rospy
from std_msgs.msg import Float32

# depend
import keyboard
import argparse
import logging
import sys
from box import Box
import time
import math

# debug
import ipdb

class movement:
    def __init__(self, max_speed=10, acc_factor=0.05):
        self.right_speed = 0
        self.left_speed = 0
        self.max_speed = max_speed
        self.acc_factor = acc_factor
    
    def right_speed_up(self):
        self.right_speed += self.acc_factor
        self.right_speed = self.limit_speed(self.right_speed,1)
    
    def left_speed_up(self):
        self.left_speed += self.acc_factor
        self.left_speed = self.limit_speed(self.left_speed,1)
    
    def right_slow_down(self):
        self.right_speed -= self.acc_factor
        self.right_speed = self.limit_speed(self.right_speed,-1)
    
    def left_slow_down(self):
        self.left_speed -= self.acc_factor
        self.left_speed = self.limit_speed(self.left_speed,-1)

    def limit_speed(self, speed, orientation):
        if abs(speed) > self.max_speed:
            return self.max_speed*orientation
        else:
            return speed

def main(kwargs):
    rospy.init_node("keyboard_control_movement")
    cfg = Box.from_yaml(filename=kwargs.config_path)
    move = movement(**cfg.movement_desigh_parameters)

    rate = rospy.Rate(cfg.rospy_rate)
    while not rospy.is_shutdown():
        logging.info("{0} {1}".format(move.left_speed, move.right_speed))
        if keyboard.is_pressed('q'):
            move.left_speed_up()
        elif keyboard.is_pressed('a'):
            move.left_slow_down()
        elif keyboard.is_pressed("e"):
            move.right_speed_up()
        elif keyboard.is_pressed("d"):
            move.right_slow_down()
        rate.sleep()
    # while True:
    #     logging.info("{0} {1}".format(move.left_speed, move.right_speed))
    #     time.sleep(cfg.sleep_time)
    #     if keyboard.is_pressed('q'):
    #         move.left_speed_up()
    #     elif keyboard.is_pressed('a'):
    #         move.left_slow_down()
    #     elif keyboard.is_pressed("e"):
    #         move.right_speed_up()
    #     elif keyboard.is_pressed("d"):
    #         move.right_slow_down()
    #     else:
    #         continue

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