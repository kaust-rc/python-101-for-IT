#!/usr/bin/env python
#Lifted from http://stackoverflow.com/questions/2953462/pinging-servers-in-python


import os, platform


def ping_time(host):
    """
    Returns True if host responds to a ping request
    """

    # Ping parameters as function of OS
    if platform.system().lower() == "windows":
		ping_str = "-n 1"
	else:
		ping_str = "-c 1"

    # Ping
    return os.system("ping " + ping_str + " " + host) == 0
