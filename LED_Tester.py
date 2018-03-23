# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 04:38:41 2018

@author: Adam

Back LEDs
36, 38, 32, 40

Front LEDs
31, 33, 35, 37

Ordered
31, 32, 33, 35, 36, 37, 38, 40

"""

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(31, GPIO.OUT)
GPIO.setup(32, GPIO.OUT)
GPIO.setup(33, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(36, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)
GPIO.setup(40, GPIO.OUT)


def on():
	GPIO.output(31, True)
	GPIO.output(32, True)
	GPIO.output(33, True)
    GPIO.output(35, True)
    GPIO.output(36, True)
    GPIO.output(37, True)
    GPIO.output(38, True)
    GPIO.output(40, True)
    
def off():
	GPIO.output(31, False)
    GPIO.output(32, False)
    GPIO.output(33, False)
    GPIO.output(35, False)
    GPIO.output(36, False)
    GPIO.output(37, False)
    GPIO.output(38, False)
    GPIO.output(40, False)


while True:
    on()
    time.sleep(0.5)
    off()
    time.sleep(0.5)


GPIO.cleanup()
