#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import time


def mkdir(filename):
    if os.path.exists(str(filename)):
        print("Have it already!\n" + str(os.listdir('./')))
    else:
        os.mkdir(filename)
        print("Created!\n" + str(os.listdir('./')))

# mkdir(input("Filename:"))
path = os.getcwd()
while True:
    order = input('root@python:~' + path + '#')
    if order == 'ls':
        filename = os.listdir(path)  # File name list
        for i in range(len(filename)):
            file = path + '\\' + filename[i]
            statinfo = os.stat(file)  # File creation time
            if os.path.isdir(file):
                properties = '<DIR>'
                size = '\t'
            else:
                properties = ''
                size = str(os.path.getsize(file)) + '\t'
            data = '%04d-%02d-%02d\t%02d:%02d\t' % time.localtime(statinfo.st_mtime)[0:5]
            print('%s%5s%10s%-10s' % (data, properties, size, filename[i]))
        print(os.stat(path))
    if order == 'cd ..':
        path = os.path.dirname(path)
    elif order[0:3] == 'cd ':
        tmp = path + '\\' + order[3:]
        if not os.path.exists(tmp):
            print('The system can not find the specified path.')
            continue
        path = tmp
    if order == 'exit':
        break
