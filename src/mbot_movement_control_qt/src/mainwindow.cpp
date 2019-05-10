#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    connect(ui->verticalSlider_left,SIGNAL(valueChanged(int)),this,SLOT(update_left_speed(int)));
    connect(ui->verticalSlider_right,SIGNAL(valueChanged(int)),this,SLOT(update_right_speed(int)));
}

void MainWindow::update_left_speed(int speed){
    ui->lcdNumber_left->display(speed);
    speeds_value.speed_of_left_motor = speed;
    speeds_pub.publish(speeds_value);
}

void MainWindow::update_right_speed(int speed){
    ui->lcdNumber_right->display(speed);
    speeds_value.speed_of_right_motor = speed;
    speeds_pub.publish(speeds_value);
}

MainWindow::~MainWindow()
{
    delete ui;
}