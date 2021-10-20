#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import datetime
import time


def stamp2time(time_stamp):
    target_time = datetime.datetime.utcfromtimestamp(int(time_stamp)).strftime("%Y-%m-%d %H:%M:%S")
    print("    " + time_stamp + " => " + target_time)


def time2stamp(str_time):
    time_str = time.strptime(str(str_time), "%Y-%m-%d %H:%M:%S")
    stamp_time = int(time.mktime(time_str))
    print("    ", end="")
    print(str_time, end=" => ")
    print(stamp_time)
