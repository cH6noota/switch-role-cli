from show_role import *
import urllib.parse
import json
from Crypto.Util.Padding import pad
from Crypto.Cipher import AES
import sqlite3
from module import *
import sys
from git_controle import *

def val_isit(l, index):  
    index= int(index) if isint(index) else None
    try:
        l[index]
        return True
    except:
        return False


args = sys.argv

if len(args)==3:
    index = args[2]
else:
    index = input("Index :")

index = index.replace(" ","").replace("　","")

data = chrome_cookies()
dic = data[0]
key = data[1]


d_list=dic["rl"]
d_list = sorted(d_list, key=lambda x:x['a'])

target = d_list[int(index)] if val_isit(d_list, index) else None
        
if target == None:
    sys.exit("Index not found: "+index)


dic["rl"].remove(target)
print("{:<6} {:<18} {:<28} {:<35} {:<8}".format('Index', 'Account id','Role name', 'View name', 'Color'))
print("{:<6} {:<18} {:<28} {:<35} {:<8}".format('-'*6,'-'*18,'-'*28, '-'*35, '-'*8))
print("{:<6} {:<18} {:<28} {:<35} {:<8}".format(index, target["a"], target["r"], urllib.parse.unquote(target["d"]), target["c"]))
tmp = input("Proceed [y/n]?")

while (tmp.lower() =="y" or tmp.lower() =="n") == False:
    tmp = input("Proceed [y/n]?")

if tmp.lower()=="n":
    sys.exit()



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


message = "{}:{} add ".format(index, target["d"])
git_add(message)
