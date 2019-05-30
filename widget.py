# Arduino Simulator
# CSE1010 Homework 8, Spring 2019
# Alex Tomczuk
# April 26, 2019
# TA: Yijue Wang
# Lab section: 002
# Instructor: Raafat Elfouly

class Widget:
    def __init__(self, n):
        self.n = n # single memmber variable
        print('Set n to', n)

    def f(receiver): # method 1
        print('My value is', receiver.n)

    def who(receiver): # method 2
        print('The receiver is', receiver)


    
