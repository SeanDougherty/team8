import datetime
import time
from Clock import Clock

c = Clock()
print (c)
print ("Starting...")
c.start_stop()
for i in range(4):
    time.sleep(2)
    print (c)
print ("Stopping...")
c.start_stop()
for i in range(4):
    time.sleep(2)
    print (c)
print ("Starting...")
c.start_stop()
for i in range(4):
    time.sleep(2)
    print (c)
print ("Resetting...")
c.reset()
print (c)
