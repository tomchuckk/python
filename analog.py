# Arduino Simulator
# CSE1010 Homework 8, Spring 2019
# Alex Tomczuk
# April 26, 2019
# TA: Yijue Wang
# Lab section: 002
# Instructor: Raafat Elfouly

import random

'''
Replicates a single analog pin on the Arduino:

*value can be read in range [0, 1020]
*value can be written in range [0, 255]
'''

class Analog:

    def __init__(self):
        # default is random value in range [0, 1023], but tends to be in range center 
        self._value = 0
        for n in range(16):
            self._value += random.randint(0, 63)

    def read(self):
        # returns value of analog pin
        return self._value

    def write(self, value):
        # forces value to be 0 if <= 0 or 255 if >= 255 & converts to [0, 1020]
        self._value = 0
        if value <= 0:
            self._value = 0
        if value >= 255:
            self._value = 255 * 4
        else:
            self._value = self._value * 4

    def set_value(self, value):
        # accepts value [0, 1023] and forces it to be in range if not
        if 0 <= value <= 1023:
            self._value = value
        if value <= 0:
            self._value = 0
        if value >= 1023:
            self._value = 1023
        return self._value
        
