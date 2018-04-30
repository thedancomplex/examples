import motor_set as ms
import time

while(1):
  ms.set(5)
  print 5
  time.sleep(5)
  ms.set(-5)
  print -5
  time.sleep(5)
