#!/usr/bin/python
#Filename:cat.py

helpString = '''\
This program prints files to the standard output.
Any number of files can be specified.
Options include:
--version : Prints the version number
--help : Display this help'''

import sys

def readfile(filename):
    '''Print a file to the standard output.'''
    f = file(filename)
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print line,
    f.close()

#Script start from here
if len(sys.argv) < 2:
    print 'No action specified.'
    sys.exit()

if sys.argv[1].startswith('--'):
    option = sys.argv[1][2:]
    if option == 'version' or option == 'v':
        print 'Version 1.2'
    elif option == 'help' or option == 'h':
        print helpString
    else:
        print 'Unknown option.'
    sys.exit()
else:
    for filename in sys.argv[1:]:
        readfile(filename)

print 'Done'
