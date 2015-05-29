#!/usr/bin/env python    #Run in Unix/Linux/Mac
# -*- coding: utf-8 -*-

' a test module '    #Module Notes

__author__ = 'Mixter Jim'    #Auther

import sys

def hi():
    args = sys.argv
    if len(args) == 1:
        print 'Hey guy!'
    elif len(args) == 2:
        print 'Hey %s!' % args[1]
    else:
        print 'Too many arguments!'

if __name__ == '__main__':    #test
    hi()
    
#This is a module document.
#Create it and saved as 'Module.py'.
#Create '__init__.py' in the same directory.
#Open the Python Shell and input 'import Module'.
    #Python will create 'Module.pyc'.
#Now,you can use the Module.
    #Module.hi()

#'python Module.py Jim' in cmd
