import os

result = os.popen("sc query MySQL57").read()
if "RUNNING" in result:
    print("The Service started Succesivlly")
