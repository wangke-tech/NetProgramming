#!/usr/bin/env python
# encoding: utf-8

import sys
import socket
import getopt
import threading
import subprocess

listen = False
command = False
upload = False
execute = ''
target = ''
upload_destination = ''
port = 0

def usage():
    print 'BHP NET Tool'
    print

    print 'Usage: bhpnet.py -t target_host -p port'
    print '-l --listen           -listen on [host]:[port] for incoming connections'
    print '-e --execute          -execute the given file upon receiving a connection'
    print '-c --command          -initialize a command line'
    print '-u --upload=distination   -upon receiving connection upload a file and write to [destination]'

    print
    print

    print 'Examples:'
    print 'bhpnet.py -t 192.168.0.1 -p 5555 -l -c'
    print 'bhpnet.py -t 192.168.0.1 -p 5555 -l -u=c:\\target.exe'
    print 'bhpnet.py -t 192.168.0.1 -p 5555 -l -e=\"cat /etc/passwd'
    print 'echo ABCDEFGHI | ./bhpnet.py -t 192.168.11.12 -p 135'
    sys.exit(0)

def main():
    global listen
    global port
    global execute
    global command
    global upload_destination
    global target

    if not len(sys.argv[1:]):
        usage()
    # 读取命令行选项
    try:
        opts,args = getopt.getopt(sys.argv[1:],'hle:t:p:cu:',['help','listen','execute','target','command','upload'])
    except getopt.GetoptError as err:
        print str(err)
        usage()
    for o,a in opts:
        if o in ('-h','--help'):
            usage()
        elif o in ('-l','--listen'):
            listen = True
        elif o in ('-e','-execute'):
            execute = True
        elif o in ('-c','--commandshell'):
            command = True
        elif o in ('-u','--upload'):
            upload_destination = a
        elif o in ('-t','--target'):
            target = a
        elif o in ('-p','--port'):
            port = int(a)
        else:
            assert False,"Unhandled Opinion"


