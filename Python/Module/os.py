#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import time


def mkdir(filename):
    if os.path.exists(str(filename)):
        print("Subdirectory or file %s already exists." % filename)
    else:
        os.mkdir(filename)


def rm(filename):
    if os.path.exists(str(filename)):
        os.rmdir(filename)


def ls():
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


def cd(filename, path):
    if order[3:] == '..':
        path = os.path.dirname(path)
        return path
    else:
        tmp = path + '\\' + order[3:]
        if not os.path.exists(tmp):
            print('The system can not find the specified path.')
            return path
        path = tmp
        return path


path = os.getcwd()
while True:
    order = input('root@python:~' + path + '#')
    if order == 'ls':
        ls()
    if order[0:3] == 'cd ':
        path = cd(order[3:], path)
    if order[0:6] == 'mkdir ':
        mkdir(path + '\\' + order[6:])
    if order[0:3] == 'rm ':
        rm(path + '\\' + order[3:])
    if order == 'exit':
        break
