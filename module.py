from os.path import expanduser
def isint(s):  
    try:
        int(s)  
    except ValueError:
        return False
    else:
        return True

def sql_path():
    home = expanduser("~/.aws-sw") + "/"
    with open(home+".env_path" , "r") as f:
        s = f.read()
    return s.replace("\n","")
