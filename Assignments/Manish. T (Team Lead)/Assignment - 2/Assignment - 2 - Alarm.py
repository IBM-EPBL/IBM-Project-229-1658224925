# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 20:44:31 2022

@author: Manish
"""
import random

def alarm():
    print("----------------------------")
    print(" Alert! Temperature is High ")
    print("----------------------------")
    
def display(temp, hum):
    print("Temperature : ", temp)
    print("Humidity : ", hum)

while True:
    ch = input("Do you want to proceed (y/n) : ")
    if ch == 'y' or ch == 'Y':
        hum = random.randint(0, 100)
        temp = random.randint(0, 100)
        if temp > 35:
            alarm()
            display(temp, hum)
        else:
            display(temp, hum)
    else:
        break