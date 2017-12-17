#!/usr/bin/env python
import os


def crawl_dirname():
    path = r"D:\android-sdk_r25.2.5-windows"
    path_list = os.listdir(path)
    print(path_list)
    fp = open("myfile.txt","wb")
    for i in path_list:
        fp.write("{}\n".format(i).encode("utf-8"))
    fp.close()
    abspath=os.path.abspath("myfile.txt")
    return abspath

print(crawl_dirname())