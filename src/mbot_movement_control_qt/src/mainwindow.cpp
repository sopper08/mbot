#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    init();

    connect(ui->pushButton_up, SIGNAL(clicked()), this, SLOT(button_up()));
    connect(ui->pushButton_down, SIGNAL(clicked()), this, SLOT(button_down()));
    connect(ui->pushButton_right, SIGNAL(clicked()), this, SLOT(button_right()));
    connect(ui->pushButton_left, SIGNAL(clicked()), this, SLOT(button_left()));
    connect(ui->pushButton_stop, SIGNAL(clicked()), this, SLOT(button_stop()));
}

void MainWindow::init(){
    /* init_parameters */
    display_and_pub_speeds();
    /* init_icon */
    setIcon(ui->pushButton_up, tr("/home/sopper08/icon/up-arrow.png"));
    setIcon(ui->pushButton_down, tr("/home/sopper08/icon/down-arrow.png"));
    setIcon(ui->pushButton_right, tr("/home/sopper08/icon/forward.png"));
    setIcon(ui->pushButton_left, tr("/home/sopper08/icon/back.png"));
    setIcon(ui->pushButton_stop, tr("/home/sopper08/icon/stop.png"));
}

void MainWindow::setIcon(QPushButton* btn, QString img_path){
    QPixmap pixmap(img_path);
    QIcon buttonIcon(pixmap);
    btn->setIcon(buttonIcon);
    btn->setIconSize(btn->size()*0.8);
}

void MainWindow::button_up(){
    linear_x += 1;
    display_and_pub_speeds();
}

void MainWindow::button_down(){
    linear_x -= 1;
    display_and_pub_speeds();
}

void MainWindow::button_right(){
    angular_z += 1;
    display_and_pub_speeds();
}

void MainWindow::button_left(){
    angular_z -= 1;
    display_and_pub_speeds();
}

void MainWindow::button_stop(){
    linear_x = 0;
    angular_z = 0;
    display_and_pub_speeds();
}

void MainWindow::display_and_pub_speeds(){
    ui->lcdNumber_x->display(linear_x);
    ui->lcdNumber_az->display(angular_z);
    nh.setParam("speeds_linear_x", linear_x);
    nh.setParam("speeds_angular_z", angular_z);
}

MainWindow::~MainWindow()
{
    delete ui;
}