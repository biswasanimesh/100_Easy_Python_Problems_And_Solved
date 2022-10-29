import os.path, time
print (time.ctime(os.path.getatime("test.txt")))
print(time.ctime(os.path.getctime("text.txt")))