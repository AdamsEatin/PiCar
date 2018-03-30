#!/usr/bin/env python
"""
@author: Adam Eaton

Controller File for PiCar Functions

Back LEDs : 32, 36, 38, 40
Front LEDs: 31, 33, 35, 37

GPIO 11 - Front Left Wheel Backward
GPIO 13 - Both Right Wheels Forward
GPIO 15 - Both Right Wheels Backward
GPIO 22 - Front Left Wheel Forward
"""

import RPi.GPIO as GPIO
import time

# Setting GPIO Mode and disabling warnings to prevent runtime errors
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# Initiliase GPIO Pins for output
def init():
    # Motor Pins
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)
    GPIO.setup(22, GPIO.OUT)
    
    # LED Pins
    GPIO.setup(31, GPIO.OUT)
    GPIO.setup(32, GPIO.OUT)
    GPIO.setup(33, GPIO.OUT)
    GPIO.setup(35, GPIO.OUT)
    GPIO.setup(36, GPIO.OUT)
    GPIO.setup(37, GPIO.OUT)
    GPIO.setup(38, GPIO.OUT)
    GPIO.setup(40, GPIO.OUT)
    

# Motor related functions
def drive_forward(tval):
    GPIO.output(11, False)
    GPIO.output(13, True)
    GPIO.output(15, False)
    GPIO.output(22, True)
    time.sleep(tval)
    
def drive_left(tval):
    GPIO.output(11, True)
    GPIO.output(13, True)
    GPIO.output(15, False)
    GPIO.output(22, False)
    time.sleep(tval)
    
def drive_right(tval):
    GPIO.output(11, False)
    GPIO.output(13, False)
    GPIO.output(15, True)
    GPIO.output(22, True)
    time.sleep(tval)
    
def drive_back(tval):
    GPIO.output(11, True)
    GPIO.output(13, False)
    GPIO.output(15, True)
    GPIO.output(22, False)
    time.sleep(tval)
    
def drive_stop(tval):
    GPIO.output(11, False)
    GPIO.output(13, False)
    GPIO.output(15, False)
    GPIO.output(22, False)
    time.sleep(tval)
    
    
# LED Related Functions
def front_lights():
    GPIO.output(31, True)
    GPIO.output(33, True)
    GPIO.output(35, True)
    GPIO.output(37, True) 
    
def left_lights():
    GPIO.output(32, True)
    GPIO.output(35, True)
    GPIO.output(37, True)
    GPIO.output(40, True)
    
def right_lights():
    GPIO.output(31, True)
    GPIO.output(33, True)
    GPIO.output(36, True)
    GPIO.output(38, True)
    
def back_lights():    
    GPIO.output(32, True)
    GPIO.output(36, True)
    GPIO.output(38, True)
    GPIO.output(40, True)

def back_lights_off():
    GPIO.output(32, False)
    GPIO.output(36, False)
    GPIO.output(38, False)
    GPIO.output(40, False)
    
def all_lights_on():
    GPIO.output(31, True)
    GPIO.output(32, True)
    GPIO.output(33, True)
    GPIO.output(35, True)
    GPIO.output(36, True)
    GPIO.output(37, True)
    GPIO.output(38, True)
    GPIO.output(40, True)

def all_lights_off():
    GPIO.output(31, False)
    GPIO.output(32, False)
    GPIO.output(33, False)
    GPIO.output(35, False)
    GPIO.output(36, False)
    GPIO.output(37, False)
    GPIO.output(38, False)
    GPIO.output(40, False)
    
    
# Controlling Functions
def forward():
    drive_stop(0.060)
    back_lights_off()
    drive_forward(0.060)
    front_lights()
    
def left():
    drive_stop(0.060)
    all_lights_off()
    drive_left(0.060)
    left_lights()
    
def right():
    drive_stop(0.060)
    all_lights_off()
    drive_right(0.060)
    right_lights()

def back():
    drive_stop(0.060)
    all_lights_off()
    drive_back(0.060)
    front_lights()
    back_lights()
    
def stop():
    drive_stop(0.060)
    all_lights_off()