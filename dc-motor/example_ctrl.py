import motor_set as ms
import time


# Set the current open-loop velocity to 1.23456

ms.set(1.23456)

# Get the current angular position - note: angular position only updates after you have set the new open=loop velocity value

theta = ms.get()
  
