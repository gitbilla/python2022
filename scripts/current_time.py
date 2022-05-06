#!/usr/bin/python
import time;
localtime = time.localtime(time.time())   # this will print informal time
print " Local current time :", localtime
print "****************************************";
localtime = time.asctime(time.localtime(time.time()) )
print "Local current time:", localtime
print " *****************************************";
print " Getting calendar for a month ";
import calendar;
cal = calendar.month(2018, 1)
print " Calendar for Jan 2018";
print cal;
