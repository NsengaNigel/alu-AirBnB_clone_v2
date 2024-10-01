#!/usr/bin/python3
"""
Fabric script that creates and distributes an archive to the web servers
"""

from fabric.api import env, local, put, run
from datetime import datetime
import os

env.hosts = ['54.146.239.100', '18.209.46.120']  # Replace with your server IPs


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder
    """
    try:
        if not os.path.exists("versions"):
            local("mkdir versions")
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_path = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(archive_path))
        return archive_path
    except Exception:
        return None


def do_deploy(archive_path):
    """
    Distributes an archive to the web servers
    """
    if not os.path.exists(archive_path):
        return False

    try:
        file_name = os.path.basename(archive_path)
        folder_name = "/data/web_static/releases/" + file_name.split('.')[0]

        put(archive_path, "/tmp/")
        run('mkdir -p {}'.format(folder_name))
        run('tar -xzf /tmp/{} -C {}/'.format(file_name, folder_name))
        run('rm /tmp/{}'.format(file_name))
        run('mv {}/web_static/* {}/'.format(folder_name, folder_name))
        run('rm -rf {}/web_static'.format(folder_name))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(folder_name))
        print("New version deployed!")
        return True
    except Exception:
        return False


def deploy():
    """
    Creates and distributes an archive to the web servers
    """
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
