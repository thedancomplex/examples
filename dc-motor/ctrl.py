import motor_set as ms
import time

theta_d = 0.0
i = 0
sw = 0
while(1):
  i = i+1
  theta = ms.get()
  e = theta_d - theta
  k = 100.0
  v = k*e
  ms.set(v)
  time.sleep(0.05)
  #print theta
  if i > 100:
      if sw == 0:
        theta_d = theta_d + 5
        sw = 1
      else: 
        theta_d = theta_d - 5
        sw = 0
      i = 0
  
