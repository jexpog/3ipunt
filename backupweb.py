#!/usr/bin/python3

import os, time, shutil, sys, tarfile, subprocess, traceback, datetime

def controlFolder():

    dir_to_search = "/var/backup_db/"
    for dirpath, dirnames, filenames in os.walk(dir_to_search):
        for file in filenames:
            curpath = os.path.join(dirpath, file)
            file_modified = datetime.datetime.fromtimestamp(os.path.getmtime(curpath))
            if datetime.datetime.now() - file_modified > datetime.timedelta(days=15):
                os.remove(curpath)


def backupWeb():
    try:
        timestamp = str(int(time.time()))
        tar = tarfile.open("/var/backup_web/backupweb"+timestamp+".bz2", "w:bz2")
        for filedir in os.listdir("/var/www/html/"):
            tar.add(os.path.join("/var/www/html/", filedir), arcname=filedir)
        tar.close()
    except:
        print("Error while creating tar archive: backupweb")
        return False
    return "/var/backup_web/backupweb"+timestamp


if __name__ == '__main__':

    # Delete file more 15 day
    controlFolder()
    # Create DB
    backupWeb()

