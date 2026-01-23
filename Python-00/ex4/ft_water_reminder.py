#!/usr/bin/env python3

def ft_water_reminder():
    last_watered = (int(input("Ways sice last watering: ")))
    if last_watered <= 2:
        print("Plants are fine")
    else:
        print("Water the plants!")
