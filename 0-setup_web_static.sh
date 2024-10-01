#!/usr/bin/env bash
# Script to set up web servers for deployment of web_static

# Update package lists and install Nginx if not already installed
sudo apt-get update
sudo apt-get install -y nginx

# Create necessary directories if they don't exist
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create a fake HTML file for testing
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create symbolic link, removing the old one if it exists
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration to serve content from /data/web_static/current/
sudo sed -i '/^\tserver_name/ a \\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default

# Restart Nginx to apply changes
sudo service nginx restart

# Exit script successfully
exit 0
