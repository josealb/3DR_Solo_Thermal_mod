#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
© Copyright 2017, MBDEV SAS, ZCOPTERS.
syncGimbalwithThermal.py:

Synchronizes GoPro and Thermal gimbals by reading GoPro Gimbal state and setting PWM output for the thermal 
camera servo.
For more infomation: jose.alberto.soler@zcopters.com
"""
from dronekit import connect, VehicleMode
from dronekit import mavutil
import time
import exceptions
previousOutput=1000
gimbalHeading=0
while True:
    try:
        vehicle = connect('0.0.0.0:14550')#, wait_ready=True)
    except:
        continue
    break
while True:
    if vehicle.gimbal.pitch is not None:
        gimbalHeading = vehicle.gimbal.pitch
    # sleep so we can see the change in map
    time.sleep(0.02)
    currentOutput=590+(10.789*gimbalHeading*-1)
    servoOutput=(currentOutput*2+previousOutput*8)/10
    previousOutput=servoOutput
    #msg=vehicle.message_factory.command_long_encode(0,0,mavutil.mavlink.MAV_CMD_DO_SET_SERVO, 0,7,servoOutput,0,0,0,0,0)
    #vehicle.send_mavlink(msg)
    vehicle.channels.overrides['7'] = servoOutput
    print "   Gimbal Pitch: %s" % gimbalHeading
    print "   PWM output: %s" % servoOutput

print("Completed")




