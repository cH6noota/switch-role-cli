from os.path import expanduser

home = expanduser("~/.aws-sw") + "/"
with open(home+"help.txt", "r") as f:
    s = f.read()
print(s)