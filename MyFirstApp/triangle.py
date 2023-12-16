#!/usr/bin/env python
import math
import time
from flyt_python import api
drone = api.navigation(timeout=120000) # instance of flyt droneigation class

#at least 3sec sleep time for the drone interface to initialize properly
time.sleep(3)

print 'taking off'
drone.take_off(10.0)

print ' going along the setpoints'
x=math.sin(60 * 3.124/180) *  10
y=math.cos(60 * 3.124/180) * 10
drone.position_set(x, y, 0, relative=True)
drone.position_set(-x,y, 0, relative=True)
drone.position_set(0,-10, 0, relative=True)
print 'Landing'
drone.land(async=False)

#shutdown the instance
drone.disconnect()
