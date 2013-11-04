#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import time
from sys import stdout

# sleep the programe 1,2,3,... seconds
def sleep(sec):
    
    t = int(time()) # get initial time as seconds
    # when the real time greater than initial time + parameter seconds
    # break while and exit from function
    while True:
        if time()>t+1:
            break
        

# replace seconds to clock h:m:s (00:00:00)
def getClock(s):
    clock = ""
    clock+= "%02d:" % (s/3600,) # find hours
    s = s%3600 # decrement seconds
    clock+= "%02d:" % (s/60,) # find minutes
    s = s%60 # decrement seconds
    clock+= "%02d" % (s,) # find seconds
    return clock # return clock as (h:m:s)



csec = 0 # initial seconds
while True:
    
    stdout.write( " Timer: {0} \r".format( getClock(csec) ) ) # print " Timer: (00:00:00)"
    stdout.flush() # do "\r" Carriage return
    
    sleep(1) # wait second
    
    csec+=1 # increment initial seconds
