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
    locdir = "/var/www/html/"
    remdir = "/var/backup_web/backupweb"
    try:
        timestamp = str(int(time.time()))
        tar = tarfile.open(remdir+timestamp+".bz2", "w:bz2")
        for filedir in os.listdir(locdir):
            tar.add(os.path.join(locdir, filedir), arcname=filedir)
        tar.close()
        print("Backup done")
    except:
        print("Backup web failed")
        return False
    return "/var/backup_web/backupweb"+timestamp


if __name__ == '__main__':

    # Delete file more 15 day
    controlFolder()
    # Create DB
    backupWeb()


