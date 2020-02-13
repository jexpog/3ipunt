#!/usr/bin/python3

import os
import time
import datetime
import subprocess

def controlFolder():

    dir_to_search = "/var/backup_db/"
    for dirpath, dirnames, filenames in os.walk(dir_to_search):
        for file in filenames:
            curpath = os.path.join(dirpath, file)
            file_modified = datetime.datetime.fromtimestamp(os.path.getmtime(curpath))
            if datetime.datetime.now() - file_modified > datetime.timedelta(days=15):
                os.remove(curpath)


def backupDb(mysqluser , mysqlpass):
    try:
        timestamp = str(int(time.time()))
        p = subprocess.Popen(
            "mysqldump -u " + mysqluser + " -p" + mysqlpass +" moodle > /var/backup_db/moodle_"+ timestamp + ".sql",
            shell=True)
        p.communicate()
        if (p.returncode != 0):
            raise
        print("Backup done")
    except:
        print("Backup failed")



if __name__ == '__main__':

    # Delete file more 15 day
    controlFolder()
    # Create DB
    backupDb("moodleuser", "moodlepass")

