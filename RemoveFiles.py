import time
import os
import shutil

path = input ("please enter the path for your folder: ")
days = 30

time.time(days)

if os.path.exists(path+"/"+ext):
   os.walk(path)
   os.path.join()

else:
    print("path not found")

ctime=os.stat(path).st_ctime
return ctime

if ctime>days:
    os.remove(path)
    shutil.rmtree()






