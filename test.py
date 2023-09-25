# -*- coding: UTF-8 -*-
from dronekit import connect, Command, LocationGlobal, VehicleMode, LocationGlobalRelative
from collections import deque
from pymavlink import mavutil
import time, sys, argparse, math
import numpy as np
import cv2, imutils


print("Baglaniliyor")
usb-id = "/dev/serial/by-id/usb-Hex_ProfiCNC_CubeOrange_310024001551393334373535-if00"
baglanti_yolu = "127.0.0.1:14550"  #sitl(sim)
rasp1 = "/dev/ttyACM0"   #jetson usb
rasp2 = "/dev/ttyAMA0"   # rasp son kullanilan
conect = "/dev/ttyUSB0"   #usb
con = "/dev/serial0"  #serial
pc = 'com7'          #windows pc
pc1 = 'com14'
pc2 = 'com6'

global drone
drone = connect(pc, wait_ready=True)
global vehicle
vehicle = drone


# ~ while not vehicle.armed:
# ~ print(" Waiting for arming...")
# ~ time.sleep(1)


vehicle.armed = True
time.sleep(5)
vehicle.mode = VehicleMode("GUIDED")
while not vehicle.armed:
    print(" Waiting for arming...")
    time.sleep(1)

vehicle.simple_takeoff(7)

while True:
    #print(" Altitude: ", vehicle.location.global_relative_frame.alt)
    if vehicle.location.global_relative_frame.alt >= 7 * 0.95:
        break
    time.sleep(1)


point1 = LocationGlobalRelative(-35.36283760, 149.16515196, 7)
point2 = LocationGlobalRelative(-35.36274474, 149.16513098, 7)
point3 = LocationGlobalRelative(-35.36274230, 149.16492722, 7)
# point4 = LocationGlobalRelative(38.7950358, 35.6152222, 7)
# point5 = LocationGlobalRelative(38.7950413, 35.6154070, 7)

vehicle.airspeed = 3
vehicle.groundspeed = 7


vehicle.mode = VehicleMode("RTL")
time.sleep(10)
