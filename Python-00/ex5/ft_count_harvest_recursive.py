#!/usr/bin/env python3

def ft_count_harvest_recursive(grow_time=None, day=1):
    if grow_time is None:
        grow_time = int(input("Days until harvest: "))
    if day <= grow_time:
        print("Day ", day)
        ft_count_harvest_recursive(grow_time, day + 1)
    else:
        print("Harvest time!")
