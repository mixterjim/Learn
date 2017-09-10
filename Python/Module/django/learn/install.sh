#!/bin/bash
sudo apt-get install python3 python3-dev python3-pip nginx -y
python3 -m pip install django uwsgi -i https://pypi.tuna.tsinghua.edu.cn/simple
echo "
[uwsgi]
socket = $PWD/learn.sock
chdir           = $PWD
module          = learn.wsgi
master          = true
processes       = 4
chmod-socket    = 666
vacuum          = true
" > uwsgi.ini
echo "
upstream django {
    server unix://$PWD/learn.sock;
}
server {
    listen 8000;
    server_name 192.168.11.123;
    charset utf-8;
    access_log /var/log/nginx/learn_access.log;
    error_log /var/log/nginx/learn_error.log;
    client_max_body_size 75M;
    location /media  {
        alias $PWD/media;
    }
    location /static {
        alias $PWD/static;
    }
    location / {
        uwsgi_pass django;
        include $PWD/uwsgi_params;
    }
}
" > learn_nginx.conf
sudo ln -s $PWD/learn_nginx.conf /etc/nginx/sites-enabled/
python3 manage.py collectstatic
sudo /etc/init.d/nginx restart
