#include "mainwindow.h"
#include "ui_mainwindow.h"
#include<QUrl>
MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    // = new QWebEngineView;
    //view->setLayout(ui->horizontalLayout);
    //view->page()->load(QUrl("localhost:8080/map.html"));
    //view->load(QUrl("localhost:8080/map.html"));
    //view->show();
    //ui->horizontalLayout->addWidget(view);
}

MainWindow::~MainWindow()
{
    delete ui;
}


void MainWindow::on_pushButton_clicked()
{
    dialog=new Dialog(this);
    dialog->setModal(true);
    dialog->show();

}

