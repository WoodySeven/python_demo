#!/usr/bin/env python
import os


def crawl_dirname(filePath):
    List = os.listdir(filePath)
    fp = open("myfile.txt", "wb")
    for i in List:
        fileList = os.path.join(filePath, i)
        fp.write("{}\n".format(fileList).encode("utf-8"))
    fp.close()


if __name__ == "__main__":
    filePath = input("please input the path to crawl: ")
    crawl_dirname(filePath)
    #print("hello")