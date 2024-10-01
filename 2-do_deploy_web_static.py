#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers
"""

from fabric.api import env, put, run, sudo
import os.path

env.hosts = ['<54.146.239.100>', '<18.209.46.120>']  # Replace with your server IPs


def do_deploy(archive_path):
    """
    Distributes an archive to the web servers
    """
    if not os.path.isfile(archive_path):
        return False

    try:
        # Upload the archive
        put(archive_path, "/tmp/")

        # Get the filename without extension
        file_name = os.path.basename(archive_path)
        folder_name = file_name.split('.')[0]

        # Uncompress the archive
        run('mkdir -p /data/web_static/releases/{}/'.format(folder_name))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.format(file_name, folder_name))

        # Remove the archive
        run('rm /tmp/{}'.format(file_name))

        # Move files
        run('mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/'.format(folder_name, folder_name))
        run('rm -rf /data/web_static/releases/{}/web_static'.format(folder_name))

        # Delete the old symbolic link
        run('rm -rf /data/web_static/current')

        # Create new symbolic link
        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'.format(folder_name))

        # Ensure correct permissions
        sudo('chown -R ubuntu:ubuntu /data/')

        # Restart Nginx
        sudo('service nginx restart')

        print("New version deployed!")
        return True
    except Exception as e:
        print(str(e))
        return False
