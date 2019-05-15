#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <iostream>
#include <QPushButton>

/* ROS */
#include <ros/ros.h>

using namespace std;

/* extern */
extern int linear_x;       /* ros Parameters */
extern int angular_z;      /* ros Parameters */

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

    void button_up();
    void button_down();
    void button_right();
    void button_left();

private:
    Ui::MainWindow *ui;
    void init();
    void setIcon(QPushButton*, QString);
    ros::NodeHandle nh; /* ros NodeHandle */
    int acc;
    int ang_acc;
    void display_and_pub_speeds();
};

#endif // MAINWINDOW_H
