#!/usr/bin/env python
import sys
from os.path import expanduser
import os

home = expanduser("~/.aws-sw") + "/"

args = sys.argv

origin_path = expanduser(
        '~/Library/Application Support/Google/Chrome/Default/Cookies'
    )

if os.path.exists(home+".env_path"):
    with open(home+".env_path" , "r") as f:
        s = f.read()
else:
    s = origin_path
    with open(home+".env_path" , "a") as f:
        f.write(origin_path)


try:
    second_args = args[1]
except:
    print("aws-sl: args not found")
    sys.exit()

if second_args == "ls":
    from show_role import show_role
    print("Set user : {}".format(s.split("Chrome")[1].split("/")[1]))
    show_role()
elif second_args == "del":
    import delete_role
elif second_args == "add":
    import add_role
elif second_args == "profile":
    import profile

elif second_args == "output":
    import output
elif "help" in second_args :
    import help