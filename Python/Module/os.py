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
        file = os.listdir(path)  # File list
        for i in range(len(file)):
            statinfo = os.stat(file[i])  # File creation time
            if os.path.isdir(file[i]):
                properties = '<DIR>'
            else:
                properties = '\t'
            data = '%d-%d-%d\t%d:%d' % time.localtime(statinfo.st_mtime)[0:5]
            print(data + "\t" + properties + "\t" + file[i],)
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
