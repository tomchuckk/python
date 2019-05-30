# Arduino Simulator
# CSE1010 Homework 8, Spring 2019
# Alex Tomczuk
# April 26, 2019
# TA: Yijue Wang
# Lab section: 002
# Instructor: Raafat Elfouly

'''
Replicates a single digital pin on the Arduino
*value is read as 0 or 1
*value can be written as 0 or 1
*mode can be set to input (0) or output(1) 
'''

class Digital:

    def __init__(self):
    # creates new digital pin
        self._dval = 0
        self._mode = 0

    def set_mode(self, val):
    # sets mode of instance to 0 or 1
     self._mode = 1

    def read(self):
    # returns value of pin (0 or 1)
        return self._dval

    def write(self, val):
    # if pin mode is "write", pin changed to 'val'
        if self._mode == 1:
            if not val:
                self._dval = 0
            else:
                self._dval = 1
