#!/usr/bin/env python3

def ft_harvest_total():
    day = 1
    total = 0
    while day <= 3:
        total = total + int(input(f"Day {day} harvest: "))
        day += 1
    print(f"Total Harvest: {total}")
