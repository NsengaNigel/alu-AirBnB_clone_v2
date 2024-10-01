#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the
web_static folder
"""

from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder
    """
    try:
        # Create the versions folder if it doesn't exist
        if not os.path.exists("versions"):
            local("mkdir versions")

        # Generate the archive name with the current date and time
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_name = "versions/web_static_{}.tgz".format(date)

        # Create the archive
        local("tar -cvzf {} web_static".format(archive_name))

        # Return the archive path if successful
        return archive_name
    except Exception:
        # Return None if an error occurs
        return None
