#!/usr/bin/env bash
#sets up your web servers for the deployment of web_static

{
sudo apt install nginx
if [ ! -d "/data/" ]; then
  sudo mkdir -p "/data/";
fi
if [ ! -d "/data/web_static/" ]; then
  sudo mkdir -p "/data/web_static/";
fi
if [ ! -d "/data/web_static/releases/" ]; then
  sudo mkdir -p "/data/web_static/releases/";
fi
if [ ! -d "/data/web_static/shared/" ]; then
  sudo mkdir -p "/data/web_static/shared/";
fi
if [ ! -d "/data/web_static/releases/test/" ]; then
  sudo mkdir -p "/data/web_static/releases/test/";
fi

echo "hello test" > "/data/web_static/releases/test/index.html"

if [ -L "/data/web_static/current" ]; then
  sudo rm "/data/web_static/current"
fi

sudo ln -s "/data/web_static/releases/test/" "/data/web_static/current"

sudo chown ubuntu:ubuntu -R /data/

sudo sed -i "/http {/a\
\n      server {\n\
                location \/hbnb_static\/ {\n\
                        alias \/data\/web_static\/current\/;\n\
                }\n\
        }" /etc/nginx/nginx.conf

sudo sed -i "s/n      server {/      server {/g" /etc/nginx/nginx.conf

sudo nginx -s reload
} &>/dev/null
