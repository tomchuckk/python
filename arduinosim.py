# Arduino Simulator
# CSE1010 Homework 8, Spring 2019
# Alex Tomczuk
# April 26, 2019
# TA: Yijue Wang
# Lab section: 002
# Instructor: Raafat Elfouly

'''
Three Major Classes:

1. ArduinoSim: each instance of this class simulates an Arduino
2. Digital: each instance of this class simulates a digital pin
3. Analog: each instance of this class simulates an analog pin

Note: each instance of ArduinoSim will contain multiple instances of Digital & Analog classes
'''

import time
import random

from analog import Analog
from digital import Digital

class ArduinoSim:

    def __init__(self):
        # ensures an instance is initialized correctly by creating analog & digital pins
        self._value = 0
        _numAnalogs = 6 # number of analog pins
        _numDigitals = 14 # number of digital pins
        analoglst = []
        digitallst = []
        for i in range(_numAnalogs):
            analoglst.append(Analog())
            self._analoglst = analoglst
        for i in range(_numDigitals):
            digitallst.append(Digital())
            self._digitallst = digitallst

    def set_value(self, value):
        # used to force analog into correct range
        if 0 <= value <= 1023:
            self._value = value
        if value <= 0:
            self._value = 0
        if value >= 1023:
            self._value = 1023
        return self._value


    def ar(self, pin):
        # returns "read" value of Analog instance if in analog pin range (6 pins)
        if pin >= 0 and pin < 6:
            self._value = random.randint(0, 1024)
            return self._value
        else:
            pass

    def dr(self, pin):
        # returns "read" value of Digital instance if in digital pin range (14 pins)
        if pin >= 0 and pin < 14:
            a = Digital()
            return a.read()
        else:
            pass

    def aw(self, pin):
        # "writes" value of Analog instance if in analog pin range (6 pins)
        if pin >= 0 and pin < 6:
            self.set_value(value)
        else:
            pass

    def dw(self, pin, value):
        ''' "writes" value of Digital instance if in digital pin range (14 pins)
            if pin 13, will display 'LED on' to simulate Arduino's on-board LED '''
        if pin >= 0 and pin < 14:
            self.set_value(value)
        if pin == 13:
            if self._value == 1:
                print('LED on')
            else:
                print('LED off')
        else:
            pass

    def dm(self, pin, value):
        # if pin number in correct range, finds pin with this instance & sets equal to mode value
        if pin >= 0 and pin < 14:
            if 0 <= value < 2:
                self.set_mode(value)
            else:
                pass
        else:
            pass

def blink(x):
    # sets digital pin 13 to "write' & turns on and off 5 times w/ 1 second delay
    x = ArduinoSim()
    for n in range(5):
        x.dw(13, 1)
        time.sleep(1)
        x.dw(13, 0)
        time.sleep(1)
    
import threading

def start_potentiometer(arduino):
    # simulates the turning of a potentiometer back and forth w/o stopping
    def run():
        delay = 0.002
        while True:
            # count up from 0 to 1023
            for n in range(1024):
                arduino._analoglst[0].set_value(n)
                time.sleep(delay)
            # count down from 1023 to 0
            for n in range(1023, -1, -1):
                arduino._analoglst[0].set_value(n)
                time.sleep(delay)
thread = threading.Thread()
thread.start()

def main():
    # samples pententiometer value on analog pin 0 every second
    ard = ArduinoSim()
    start_potentiometer(ard)
    for n in range(10):
        print(n, ':', ard.ar(0))
        time.sleep(1)
