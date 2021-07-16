import sys
import os
from os.path import expanduser
from module import *


def profile_num():
    num=1
    while True:
        path = expanduser(
            "~/Library/Application Support/Google/Chrome/Profile {}/Cookies".format(num)
            )
        if os.path.exists(path) == False:
            return num-1
        num+=1

def default_check(newuser):
    if newuser=="Default":
        with open(".env_path" , "w") as f:
            s = expanduser("~/Library/Application Support/Google/Chrome/{}/Cookies".format(newuser))
            f.write(s)
        sys.exit()
    return ""

args = sys.argv
max_num = profile_num()

if len(args)==3:
    newuser = args[2]
else:
    newuser= input("New user number of Default [1~{} / Default]:".format(max_num))


default_check(newuser)
newuser= int(newuser) if isint(newuser) else -1


while (0<newuser and newuser<= max_num)==False:
    newuser= input("Try new user number of Default [1~{} / Default]:".format(max_num))
    default_check(newuser)
    newuser= int(newuser) if isint(newuser) else -1

with open(".env_path" , "w") as f:
    s = expanduser("~/Library/Application Support/Google/Chrome/Profile {}/Cookies".format(newuser))
    f.write(s)