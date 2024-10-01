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

# Give ownership of the /data/ folder to the current user and group
sudo chown -R $(whoami):$(whoami) /data/

# Ensure the Nginx configuration includes the /hbnb_static/ location block
if ! grep -q "location /hbnb_static/" /etc/nginx/sites-available/default; then
    sudo sed -i '/server_name _;/a \\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default
fi

# Test the Nginx configuration for syntax errors
sudo nginx -t

# Restart Nginx to apply changes if the configuration test passed
if [ $? -eq 0 ]; then
    sudo service nginx restart
else
    echo "Nginx configuration failed. Please check your configuration."
    exit 1
fi

# Exit script successfully
exit 0
