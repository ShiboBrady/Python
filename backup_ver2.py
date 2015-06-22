#!/usr/bin/python
#Filename:backup_ver2.py

import os
import time

#1.The files and directories to be backed up.
source = ['/home/shibo/Code']

#2.The backup must be storted in a main backup file
target_dir = '/home/shibo/backup/'

#3.backup file path name
today = target_dir + time.strftime('%Y%m%d')

#4.backup file name
now = time.strftime('%H%M%S')
target = today + os.sep + now + '.zip'

#5.create backup path
if not os.path.exists(today):
    os.mkdir(today)
    print 'Successfully created directory', today

#6.zip command
zip_command = "zip -qr '%s' %s" %(target, ''.join(source))

#7.Run zip command
if os.system(zip_command) == 0:
    print 'Successful backup to', target
else:
    print 'Backup FAILED'

print 'Done'

