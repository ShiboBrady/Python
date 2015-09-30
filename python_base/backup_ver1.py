#!/usr/bin/python
#Filename:backup_ver1.py

import os
import time

#1.The files and directories to be backed up
source = ['/home/shibo/Code']

#2.The backup must be stored in a main backup directory
target_dir = '/home/shibo/backup/'

#3.The files are backed up into a zip file
target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'

#4.Use the zip command to put the files in a zip archive
zip_command = "zip -qr '%s' %s"%(target, ' '.join(source))

#5.Run the backup
if os.system(zip_command) == 0:
    print 'Successful backup to', target
else:
    print 'Backup failed.'

print 'Done'
