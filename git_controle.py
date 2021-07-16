import os
import subprocess
from subprocess import PIPE
from module import sql_path

origin_path = sql_path().split("/Cookie")[0]

if os.path.exists(origin_path+"/.git") == False:
    #os.system('git init "'+origin_path+'"' )
    proc = subprocess.run('git init "'+origin_path+'"', shell=True, stdout=PIPE, stderr=PIPE)
    proc = subprocess.run('cd "'+origin_path+'"; git add Cookies', shell=True, stdout=PIPE, stderr=PIPE)
    proc = subprocess.run('cd "'+origin_path+'"; git commit -m "first commit"', shell=True, stdout=PIPE, stderr=PIPE)


def git_add(message):
    #os.system('cd "'+origin_path+'"; git add Cookies')
    #os.system('cd "'+origin_path+'"; git commit -m "file change"')
    proc = subprocess.run('cd "'+origin_path+'"; git add Cookies', shell=True, stdout=PIPE, stderr=PIPE)
    proc = subprocess.run('cd "'+origin_path+'"; git commit -m "'+message+'"', shell=True, stdout=PIPE, stderr=PIPE)

def lole_back(num):
    for i in range(num):
        git_reset()

def git_reset():
    proc = subprocess.run('cd "'+origin_path+'"; git reset --hard HEAD^', shell=True, stdout=PIPE, stderr=PIPE)
    

