#include "mainwindow.h"
#include <QApplication>
/* ROS */
#include "ros/ros.h"
#include "std_msgs/Int8.h"
#include "mbot_movement_control_qt/speeds_msg.h"

/* msgs */
mbot_movement_control_qt::speeds_msg speeds_value;
/* publisher */
ros::Publisher speeds_pub;

int main(int argc, char *argv[])
{
    /* ROS pulisher init */
    ros::init(argc, argv, "speeds_qt_gui");
    ros::NodeHandle n;
    speeds_pub = n.advertise<mbot_movement_control_qt::speeds_msg>("speeds", 1);
    /* init std_msgs data */
    speeds_value.speed_of_left_motor = 0;
    speeds_value.speed_of_right_motor = 0;
    /* GUI part */
    QApplication a(argc, argv);
    MainWindow w;
    w.show();

    return a.exec();
}