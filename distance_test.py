#!/usr/bin/env python3
"""
@author: Adam Eaton

Script to get a reading from the distance sensor.
"""

from hcsr04sensor import sensor
import RPi.GPIO as GPIO

def main():
    trig_pin = 12
    echo_pin = 18
    
    value = sensor.Measurement(trig_pin, echo_pin, gpio_mode=GPIO.BOARD)
    raw_measurement = value.raw_distance()
    
    metric_distance = value.distance_metric(raw_measurement)
    
    return metric_distance
    
dist = main()
print(dist)
GPIO.cleanup()