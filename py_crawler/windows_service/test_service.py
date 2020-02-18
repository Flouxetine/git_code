import wmi
import time
import os


def startServer():
    # logger.info("The Service %s is starting....... "  % name)
    ber_result = os.popen("sc query MySQL57").read()
    if "RUNNING" in ber_result:
        print("The Service Already started")
    else:
        os.popen("sc start MySQL57").read()
        time.sleep(30)
        result = os.popen("sc query MySQL57").read()
        if "RUNNING" in result:
            print("The Service started Succesivlly")


c = wmi.WMI()
MySQL57_services = c.Win32_Service(StartMode="Auto",
                                   State="Stopped",
                                   Caption="MySQL57")
if MySQL57_services:
    startServer()
else:
    print("the services started")
