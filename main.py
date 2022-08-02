import argparse
import platform
import time
from datetime import datetime as dt
localhost = '127.0.0.1'


# find os function
def environment():
    my_os = platform.system()
    # if linux
    if my_os == "Linux":
        return "/etc/hosts"
    # if mac
    elif my_os == "darwin":
        return "/etc/hosts"
    # if windows
    elif my_os == "Windows":
        return r"C:\Windows\System32\drivers\etc\hosts"


# slice webSites function
def sliceWebSite(listsite):
    listsite=[localhost + '\t' + i.split("/")[2] + '\n' if i.startswith("http") else localhost+'\t'+i+'\n' for i in listsite]
    return set(listsite)


# block webSites function
def blockSite(siteToBlock):
    # send to slice webSite...
    siteToBlock = sliceWebSite(siteToBlock)
    # read from hosts file
    with open(environment(), 'r+')as hostsfile:
        lines = hostsfile.readlines()
        #  list of all lines if they start 127.0.0.1 - they sites
        lines = [line for line in lines if line.startswith('127.0.0.1')]
        # write webSite to hosts file
        [hostsfile.write(str) for str in siteToBlock.difference(lines)]
    print(f'The sites are blocked- {siteToBlock}')


# unblock webSites function
def unblockSite(siteToUnblock):
    # send to slice webSite...
    siteToUnblock = sliceWebSite(siteToUnblock)
    # read from hosts file
    with open(environment(), 'r+') as hostsfile:
        lines = set(hostsfile.readlines())
        # re-write to hosts file
        hostsfile.seek(0)
        # write to hosts file site to block
        [hostsfile.write(str) for str in lines.difference(siteToUnblock)]
        # change size of hosts file
        hostsfile.truncate()
    print(f'The sites are unblocked- {siteToUnblock}')


# time to block webSites function
def timeOfBlockSite(start, end, blink=None, ulink=None):
    start = int(start)
    end = int(end)
    # check the time....
    while True:
        if dt(dt.now().year, dt.now().month, dt.now().day, start) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, end):
            blockSite(blink)
        else:
            unblockSite(ulink)
        time.sleep(5)


# function to start....
def main():
    parser = argparse.ArgumentParser(description="My block sites script")
    parser.add_argument('--blink', '-b', action='append', help='Enter web Site to block (b \ blink) : ')
    parser.add_argument('--ulink', '-u', action='append', help='Enter web Site to unblock (u \ ulink) :')
    parser.add_argument('--start', '-s', type=int, help='Enter hour to start block (s \ start) :')
    parser.add_argument('--end', '-e', type=int, help='Enter hour to end block (e \ end) :')
    args = parser.parse_args()
    if args.blink:
       blockSite(args.blink)
    if args.ulink:
       unblockSite(args.ulink)
    if args.blink or args.ulink and args.start and args.end :
        timeOfBlockSite(args.start, args.end, args.blink, args.ulink)

if __name__ == '__main__':
    main()






