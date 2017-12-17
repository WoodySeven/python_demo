#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@author:Administrator 
@file: crawler_zhanglei.py 
@time: 2017/12/16 
""" 
import os


def file_name(file_dir):
    file_dir = "F:\github\homework"
    for root, dirs, files in os.walk(file_dir):
        print(root) #当前目录下所有文件的路径
        # print(dirs) #当前路径下所有子目录
        # print(files) #当前路径下所有非目录子文件


def crawl_dirname():
    dpath=r"D:\android-sdk_r25.2.5-windows"
    list1=os.listdir(dpath)
    print(list1)
    with open("myfile.txt","wb") as fp:
        for i in list1:
            #fp.write(i.encode("utf-8"+b'\n'))
            fp.write("{}\n".format(i).encode("utf-8"))
    # print("abs path is %s" % (os.path.abspath("myfile.txt")))
    absdir=os.path.abspath("myfile.txt")
    print(absdir)
    return absdir



if __name__=="__main__":
    crawl_dirname()
    # file_name(file_dir)