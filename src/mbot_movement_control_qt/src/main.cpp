#include "mainwindow.h"
#include <QApplication>
/* ROS */
#include "ros/ros.h"

/* ros Parameters */
int linear_x;
int angular_z;

int main(int argc, char *argv[])
{
    /* ROS pulisher init */
    ros::init(argc, argv, "speeds_qt_gui");
    /* init ros parameters */
    linear_x = 0;
    angular_z = 0;
    /* GUI part */
    QApplication a(argc, argv);
    MainWindow w;
    w.show();

    return a.exec();
}