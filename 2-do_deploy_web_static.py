#!/usr/bin/python3
"""
Fabric script that distributes an archive to the web servers
"""

from fabric.api import env, put, run
import os.path

# Define the IP addresses of your web servers
env.hosts = ['<54.146.239.100>', '<18.209.46.120>']


def do_deploy(archive_path):
    """
    Distributes an archive to the web servers
    """
    if not os.path.exists(archive_path):
        return False

    try:
        # Upload the archive
        put(archive_path, "/tmp/")

        # Get the filename without extension
        file_name = os.path.basename(archive_path)
        folder_name = "/data/web_static/releases/" + file_name.split('.')[0]

        # Uncompress the archive
        run('mkdir -p {}'.format(folder_name))
        run('tar -xzf /tmp/{} -C {}/'.format(file_name, folder_name))

        # Remove the archive
        run('rm /tmp/{}'.format(file_name))

        # Move files
        run('mv {}/web_static/* {}/'.format(folder_name, folder_name))
        run('rm -rf {}/web_static'.format(folder_name))

        # Delete the symbolic link
        run('rm -rf /data/web_static/current')

        # Create new symbolic link
        run('ln -s {} /data/web_static/current'.format(folder_name))

        print("New version deployed!")
        return True
    except Exception:
        return False
