#!/usr/bin/env python
#encoding:utf-8
import os


def crawl_dirname(filePath):
    List = os.listdir(filePath)
    fp = open("myfile.txt", "wb")
    for i in List:
        fileList = os.path.join(filePath, i)
        print(fileList)
        fp.write("{}\n".format(i).encode("utf-8"))
    fp.close()


if __name__ == "__main__":
    filePath = input("请输入要查找的目录地址")
    # crawl_dirname(filePath)
    print("hello")