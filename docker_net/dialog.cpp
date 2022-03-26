#include "dialog.h"
#include "ui_dialog.h"
#include<QValidator>
#include<QStandardItem>
#include<QDebug>
#include<fstream>
Dialog::Dialog(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::Dialog)
{
    ui->setupUi(this);
    QIntValidator *pIntValidator = new QIntValidator(this);
    pIntValidator->setRange(3, 20);
}

Dialog::~Dialog()
{
    delete ui;
}

void Dialog::on_buttonBox_accepted()
{
    QProcess *process = new QProcess();
    //QStringList argument;
    ofstream file("/home/seed/Desktop/cyber_range/docker_net/data.txt",ios::out|ios::trunc);
    int* matrix=new int(num*num);
    //argument<<"D:\\Github\\cyber_range\\docker-net\\run.sh";
    process->setWorkingDirectory("/home/seed/Desktop/cyber_range/docker_net");
    process->start("/usr/bin/bash");
    process->waitForStarted();
    process->write("./run.sh \n");
    //process->write();
    for(int i=0;i<num;i++)
    {
        for(int j=0;j<num;j++)
        {
            QModelIndex index =ui->tableView->model()->index(i,j);
            matrix[i*num+j]=ui->tableView->model()->data(index).toInt();
        }
    }
    if(!file.is_open())
    {
        qDebug()<<"fail to open this file";
    }
    for(int i=0;i<num*num;i++)
    {
        file<<matrix[i]<<"   ";
    }
}


void Dialog::on_pushButton_clicked()
{
    num=ui->lineEdit->text().toInt();
    QStandardItemModel *model = new QStandardItemModel();
    QStringList list;
    for(int i=0;i<num;i++)
        list<<QString::number(i+1);
    //qDebug()<<num;
    model->setHorizontalHeaderLabels(list);
    model->setVerticalHeaderLabels(list);
    ui->tableView->setModel(model);
    ui->tableView->horizontalHeader()->setStretchLastSection(true);
    ui->tableView->show();
}

