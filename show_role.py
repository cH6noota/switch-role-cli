import sqlite3
import urllib.parse
import keyring
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
import urllib.parse
import json
from module import *

def chrome_decrypt(encrypted_value, key=None):
    
    iv = b' ' * 16
    encrypted_value = encrypted_value[3:]
 
    def clean(x):
        return x[:-x[-1]].decode('utf8')
 
    cipher = AES.new(key, AES.MODE_CBC, IV=iv)
    decrypted = cipher.decrypt(encrypted_value)
 
    return clean(decrypted)
 
def chrome_cookies():
 
    salt = b'saltysalt'
    
    length = 16

    my_pass = keyring.get_password('Chrome Safe Storage', 'Chrome')
    my_pass = my_pass.encode('utf8')
    iterations = 1003
    #cookie_file = os.path.expanduser(
    #    '~/Library/Application Support/Google/Chrome/Default/Cookies'
    #)
    cookie_file = sql_path()
    key = PBKDF2(my_pass, salt, length, iterations)
    
    conn = sqlite3.connect(cookie_file)
    sql = 'select name, value, encrypted_value from cookies '\
            'where name=="noflush_awsc-roleInfo"'
    cookies = {}
    cookies_list = []
 
    with conn:
        for k, v, ev in conn.execute(sql):
            decrypted_tuple = (k, chrome_decrypt(ev, key=key))
            cookies_list.append(decrypted_tuple)
        cookies.update(cookies_list)
    conn.commit()
    conn.close()
    dic = None if len(cookies) == 0 else json.loads(urllib.parse.unquote(cookies["noflush_awsc-roleInfo"]))
    return dic,key


def print_role(d):
    if d==None :
        print("No Swtich role data \nPATH : {}".format(sql_path()))
        return 
    d_list=d["rl"]
    if len(d_list)==0 :
        print("No Swtich role data \nPATH : {}".format(sql_path()))
        return 
    d_list = sorted(d_list, key=lambda x:x['a'])
    print("{:<6} {:<18} {:<28} {:<35} {:<8}".format('Index', 'Account id','Role name', 'View name', 'Color'))
    print("{:<6} {:<18} {:<28} {:<35} {:<8}".format('-'*6,'-'*18,'-'*28, '-'*35, '-'*8))
    for index,i in enumerate(d_list):
        print("{:<6} {:<18} {:<28} {:<35} {:<8}".format(index, i["a"], i["r"], urllib.parse.unquote(i["d"]), i["c"]))
        print("{:<6} {:<18} {:<28} {:<35} {:<8}".format('-'*6,'-'*18,'-'*28, '-'*35, '-'*8))
    print()


def show_role():
    data = chrome_cookies()
    dic= data[0]
    #print(dic)
    print_role(dic)
    #print("\n",str(dic).replace(",","\n").replace("{","").replace("}",""),"\n")


#dic = json.loads(urllib.parse.unquote(cookies["noflush_awsc-roleInfo"]))
#print(dic)