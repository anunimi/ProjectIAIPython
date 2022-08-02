import platform
import time
from datetime import datetime as dt
localhost = "127.0.0.1"
# find os
def thisEnvironment():

    my_os = platform.system()
    print("OS in my system : ", my_os)

    if my_os == "Linux" or my_os == "Linux2":
        return "/etc/hosts"
    # mac
    elif my_os == "darwin":
        return "/etc/hosts"

    elif my_os == "Windows":
        return r"C:\Windows\System32\drivers\etc\hosts"

    elif my_os == "win64":
        return r"C:\Windows\System32\drivers\etc\hosts"

# Slice web site
def SliceWebSite(listsite):
    listsite=[localhost+'\t'+i.split("/")[2]+'\n' if i.startswith("http") else localhost+'\t'+i+'\n' for i in listsite]
    return set(listsite)

def block_site(list):
    with open(thisEnvironment(),'r+')as hostsfile:
        lines=hostsfile.readlines()
        lines = [i for i in lines if not i.startswith("#") and not i.startswith("\n")]
        print(lines)
        list=set(SliceWebSite(list))
        new=[hostsfile.write(str) for str in list if str not in lines]
        print(new)

def unblock_site(sites_to_block):
    with open(thisEnvironment(), 'r+') as hostsfile:
        lines = hostsfile.readlines()
        listSite = SliceWebSite(sites_to_block)
        hostsfile.seek(0)
        [hostsfile.write(str) for str in lines if not str in listSite]
        hostsfile.truncate()

def TimeOfBlockSite(char,start,end):
    if char == 'h':
        while True:
            if dt(dt.now().year, dt.now().month, dt.now().day,start)< dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,end):
                block_site(sites_to_block1)
            else:
                unblock_site(sites_to_block1)
    else:
        while True:
            if dt(dt.now().year, dt.now().month, start,dt.now().hour)< dt.now() < dt(dt.now().year, dt.now().month, end,dt.now().hour):
                block_site(sites_to_block1)
            else:
                unblock_site(sites_to_block1)

sites_to_block1 = [
    'www.facebook.com',  'facebook.com',
    'www.youtube.com', 'youtube.com',
    'www.gmail.com', 'gmail.com'
]
sites_to_block = [
   'www.facebook.com',  'facebook.com'
]

print("h for hours or d for days")
char=input()
print("enter start and end")
start=input()
end=input()
TimeOfBlockSite(char,start,end)

block_site(sites_to_block1)
# unblock_site(sites_to_block)
