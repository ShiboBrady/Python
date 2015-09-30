#!/usr/bin/python
#Filename:using_file.py

poem = '''\
Programming is fun 
When the work is done 
if you wanna make your work also fun: 
use Python! 
'''

filename = 'poem.txt'

f = file(filename, 'w')
f.write(poem)
f.close()

f = file(filename);
while True:
    line = f.readline()
    if len(line) == 0:
        break
    print line,

f.close()
print 'Done'
