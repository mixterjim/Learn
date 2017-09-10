#!/bin/bash
sudo /etc/init.d/nginx restart
uwsgi --ini uwsgi.ini
