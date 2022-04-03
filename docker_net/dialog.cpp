#include "dialog.h"
#include "ui_dialog.h"
#include<QValidator>
#include<QStandardItem>
#include<QDebug>
#include<fstream>
#include<cstring>
#include<queue>
#include<QMessageBox>
typedef pair<int,int> node;
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
    int* matrix=new int(num*num);
    for(int i=0;i<num;i++)
    {
        for(int j=0;j<num;j++)
        {
            QModelIndex index =ui->tableView->model()->index(i,j);
            matrix[i*num+j]=ui->tableView->model()->data(index).toInt();
        }
    }
    bool* vis=new bool[num];
    bool flag=0;
    queue<node> q;
    for(int i=0;i<num;++i)
    {
        if(flag)break;
        while(!q.empty())q.pop();
        memset(vis,0,sizeof(vis));
        vis[i]=1;
        q.push(node(-1,i));
        while(!q.empty())
        {
            if(flag)break;
            int u=q.front().second,fa=q.front().first;
            q.pop();
            for(int j=0;j<num;++j)
                if(matrix[u*num+j])
                {
                    int v=j;
                    if(v==fa)continue;
                    if(vis[v])
                    {
                        flag=1;
                        break;
                    }
                    else
                    {
                        vis[v]=1;
                        q.push(node(u,v));
                    }
                }
        }
    }
        delete[]vis;
    if(flag)
        QMessageBox::information(NULL,"error","as configuration table error",QMessageBox::Yes | QMessageBox::No,QMessageBox::Yes);
    else
    {
        QProcess *process = new QProcess();
        //QStringList argument;
        ofstream file("/home/seed/Desktop/cyber_range/docker_net/data.txt",ios::out|ios::trunc);
        //argument<<"D:\\Github\\cyber_range\\docker-net\\run.sh";
        process->setWorkingDirectory("/home/seed/Desktop/cyber_range/docker_net");
        process->start("/usr/bin/bash");
        process->waitForStarted();
        process->write("./run.sh \n");
        //process->write();
        if(!file.is_open())
        {
            qDebug()<<"fail to open this file";
        }
        for(int i=0;i<num*num;i++)
        {
            file<<matrix[i]<<"   ";
        }
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

