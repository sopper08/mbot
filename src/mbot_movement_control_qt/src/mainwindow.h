#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <iostream>

/* ROS */
#include <ros/ros.h>
#include "mbot_movement_control_qt/speeds_msg.h"

using namespace std;

extern mbot_movement_control_qt::speeds_msg speeds_value;
extern ros::Publisher speeds_pub;

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();

private slots:
    void update_left_speed(int);
    void update_right_speed(int);

private:
    Ui::MainWindow *ui;
};

#endif // MAINWINDOW_H
