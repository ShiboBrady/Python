#!/usr/bin/python
#Filename:backup_ver3.py

import os
import time

#1.source file which to be backed up.
source = ['/home/shibo/Code']

#2.target path which are backed up to.
target_dir = '/home/shibo/backup/'

#3.target path name
today = target_dir + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

#4.create target path
if not os.path.exists(today):
    os.mkdir(today)
    print 'Successfully created directory', today

#5.Get user command
comment = raw_input('Enter a comment -->')
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + \
    comment.replace(' ', '_') + '.zip'

#6.zip command
zip_command = "zip -qr '%s' %s" %(target, ''.join(source))

#7.Run zip command
if os.system(zip_command) == 0:
    print 'Successfully backed up to', target
else:
    print 'Backed up failed.'

print 'Done'
