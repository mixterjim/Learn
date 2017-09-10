#!/bin/bash
sudo /etc/init.d/nginx stop
sudo python3 $PWD/manage.py runserver 0.0.0.0:80
