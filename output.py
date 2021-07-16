from show_role import *
import urllib.parse
from module import *
from git_controle import *

data = chrome_cookies()
dic = data[0]
key = data[1]

d_list=dic["rl"]
d_list = sorted(d_list, key=lambda x:x['a'])
for i in d_list:
    print("[{}]".format(urllib.parse.unquote(i["d"]).split("  |")[0]))
    print(
        "role_arn = arn:aws:iam::{}:role/{}".format(i["a"], i["r"])
        )
    print("color = {}".format(i["c"]))
    print()