import os
import win32api
import wmi 






src = "C:\\CTIL\\dblogic\\dbLogic.dll"
if not os.path.exists(src):
    exit()

def stopservice(name):
    result = os.popen("sc query %s" % name).read()
    if "RUNNING" in result:
        logger.info("The Service %s is running........" % name)
        os.popen("sc stop %s" % name).read()
        logger.info("Stop Service ........")
        time.sleep(60)
    elif "START_PENDING" in result:
        logger.info("The Service  %s is starting........" % name)
        time.sleep(10)
        os.popen("sc stop %s" % name).read()
        logger.info("Stop Service ........")
        time.sleep(10)
    elif "STOP_PENDING" in result:
        logger.info("The Service  %s is stopping........" % name)
        time.sleep(10)
    elif "STOPPED" in result:
        logger.info("The Service  %s stopped........" % name)
    else:
        logger.info("The Service %s is in other status........" % name)

def deleteFile(filepath):
    if os.path.isfile(filepath):
        try:
            os.remove(filepath)
        except:
            print("delete File failure: %s" % filepath)
    elif os.path.isdir(filepath):
        for item in os.listdir(filepath):
            itemsrc = os.path.join(filepath, item)
            deleteFile(itemsrc)
        try:
            os.rmdir(filepath)
        except:
            print("delete Folder failure: %s" % filepath)

def startservice(name):
    logger.info("The Service %s is starting....... "  % name)
    os.popen("sc start %s" % name).read()
    time.sleep(60)
    result = os.popen("sc query %s" % name).read()
    if "RUNNING" in result:
        logger.info("The Service started Succesivlly")
