#!/usr/bin/env bash
#sets up your web servers for the deployment of web_static

apt install nginx
if [ -d "/data/" ]; then
  mkdir -p "/data/";
fi
if [ -d "/data/web_static/" ]; then
  mkdir -p "/data/web_static/";
fi
if [ -d "/data/web_static/releases/" ]; then
  mkdir -p "/data/web_static/releases/";
fi
if [ -d "/data/web_static/shared/" ]; then
  mkdir -p "/data/web_static/shared/";
fi
if [ -d "/data/web_static/releases/test/" ]; then
  mkdir -p "/data/web_static/releases/test/";
fi

echo "hello test" > "/data/web_static/releases/test/index.html"

if [ -f "/data/web_static/current" ]; then
  rm /data/web_static/current;
fi

ln -s "/data/web_static/current" "/data/web_static/releases/test/";

chown ubuntu:ubuntu -R /data/

sudo sed -i "http {/a\
	server {\
		location /hbnb_static/ {\
			alias /data/web_static/current/\
		}\
	}" /etc/nginx/nginx.conf
