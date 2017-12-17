#!/usr/bin/env python
import os

def crawl_dirname(file_path_name):
    i = os.listdir(file_path_name)
    file_path = file_path_name
    with open("myfile.txt","wb") as fp:
        for a in i:
            fp.write("{}\{}\n".format(file_path, a).encode("utf-8"))


if __name__=="__main__":
    name = str(input("请输入要查找的路径："))
    crawl_dirname(name)