# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 23:03:21 2018

@author: Adam


GPIO 11 - Front Left Wheel Backward
GPIO 13 - Both Right Wheels Forward
GPIO 15 - Both Right Wheels Backward
GPIO 22 - Front Left Wheel Forward


GPIO 35, 36, 37, 38, 40 - LEDs
"""

import RPi.GPIO as gpio
import curses
import time
import os


def init():
    gpio.setmode(gpio.BOARD)
    # Motors
    gpio.setup(11, gpio.OUT)
    gpio.setup(13, gpio.OUT)
    gpio.setup(15, gpio.OUT)
    gpio.setup(22, gpio.OUT)
    
    # LEDs
    gpio.setup(35, gpio.OUT)
    gpio.setup(36, gpio.OUT)
    gpio.setup(37, gpio.OUT)
    gpio.setup(38, gpio.OUT)
    gpio.setup(40, gpio.OUT)


def forward(tval):
    gpio.output(11, False)
    gpio.output(13, True)
    gpio.output(15, False)
    gpio.output(22, True)
    time.sleep(tval)
    
def reverse(tval):
    gpio.output(11, True)
    gpio.output(13, False)
    gpio.output(15, True)
    gpio.output(22, False)
    time.sleep(tval)
       
def turn_left(tval):
    gpio.output(11, True)
    gpio.output(13, True)
    gpio.output(15, False)
    gpio.output(22, False)
    time.sleep(tval)
      
def turn_right(tval):
    gpio.output(11, False)
    gpio.output(13, False)
    gpio.output(15, True)
    gpio.output(22, True)
    time.sleep(tval)
    
def stop(tval):
    gpio.output(11, False)
    gpio.output(13, False)
    gpio.output(15, False)
    gpio.output(22, False)
    time.sleep(tval)


def lights_on():
    gpio.output(35, True)
    gpio.output(36, True)
    gpio.output(37, True)
    gpio.output(38, True)
    gpio.output(40, True)
    
def lights_off():
    gpio.output(35, False)
    gpio.output(36, False)
    gpio.output(37, False)
    gpio.output(38, False)
    gpio.output(40, False)
    
def main(win):
    init()
    sleep_val = 0.060
    
    win.nodelay(True)
    key=""
    msg = ""
    win.clear()                
    win.addstr("Detected: ")
    
    while 1:          
        try:                 
           key = win.getkey()         
           win.clear()                
           win.addstr("Detected: ", str(key))
           #win.addstr(str(key))
           win.addstr("\n", msg)
           
           if str(key) == "w":
               forward(sleep_val)
               lights_off()
               
           elif str(key) == "s":
               reverse(sleep_val)
               lights_on()
               
           elif str(key) == "a":
               turn_left(sleep_val)
               lights_off()
               
           elif str(key) == "d":
               turn_right(sleep_val)
               lights_off()
               
           elif str(key) == "q":
               stop(sleep_val)
               lights_off()
               
           elif str(key) == "p":
               lights_off()
               gpio.cleanup()
               break           
        except Exception as e:
           # No input   
           pass         

curses.wrapper(main)