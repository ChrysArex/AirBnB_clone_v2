#!/usr/bin/env bash

# Install Nginx if not already installed
if ! command -v nginx &> /dev/null; then
    sudo apt-get update
    sudo apt-get install -y nginx
fi

# Create necessary folders if they don't exist
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo chown -R ubuntu:ubuntu /data

# Create a fake HTML file for testing
sudo touch /data/web_static/releases/test/index.html
sudo echo "<html>
  <head>
  </head>
    <body>
        Holberton School
    </body>
</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Create or recreate symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Update Nginx configuration
sudo bash -c 'cat > /etc/nginx/sites-available/default' << EOF
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    server_name _;

    location /hbnb_static {
        alias /data/web_static/current/;
    }
}
EOF

# Restart Nginx
sudo systemctl restart nginx

exit 0