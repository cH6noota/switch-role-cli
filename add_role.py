from show_role import *
import json
from Crypto.Util.Padding import pad
from Crypto.Cipher import AES
import sqlite3
import sys
from git_controle import *
import random

args = sys.argv

def parse_data(arn_origin):
    try:
        arn = arn_origin.replace("arn:aws:iam::","").replace(" ","")
        account_id = arn.split(":")[0]
        role_name = arn.split("/")[1]
        view_name = input("View name :")
        color = input("Color [Enter(ramdom)]:")
    except:
        print("Not arn format: {}".format(arn_origin))
        sys.exit()
    return account_id, role_name, view_name, color

def ramdom_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    s = '%02x%02x%02x' % (r, g, b)
    return s.upper()

def first_add():
    print("No Switch role history")
    account_id = input("Account id or Account alias:")
    role_name = input("User name :")
    return {'bn': role_name, 'ba': account_id , 'rl': []}


data = chrome_cookies()
dic= data[0]
key = data[1]


# 初めてのadd
if  dic==None:
    sys.exit("sw : No Switch role history\nPlease login https://aws.amazon.com/")

if len(args)==3:
    account_id, role_name, view_name, color = parse_data(args[2])
else:
    account_id = input("Account id :")
    role_name = input("Role name :")
    view_name = input("View name :")
    color = input("Color [Enter(ramdom)]:")
while view_name=="":
    view_name = input("Try view name :")
color = color if color !="" else ramdom_color()

new = { 'a': account_id,
        'r': role_name,
        'd': view_name,
        'c': color
    }


dic["rl"].append(new)

new_data = urllib.parse.quote(json.dumps(dic))

iv = b' ' * 16
cipher = AES.new(key, AES.MODE_CBC, IV=iv)
decrypted = cipher.encrypt(pad(new_data.encode('utf-8'), AES.block_size))
en_data= "v10".encode('utf-8') + decrypted 


origin_path = sql_path()
conn = sqlite3.connect(origin_path)
sql = 'update cookies set  encrypted_value=? where  host_key like "%{}%" and  name=="noflush_awsc-roleInfo" '.format("aws.amazon.com")

c = conn.cursor()
try:
    c.execute(sql, (en_data, ))
except sqlite3.Error as e:
    print("error",e.args[0])

conn.commit()
conn.close()

message = "{}:{} add ".format(account_id, view_name)
git_add(message)


