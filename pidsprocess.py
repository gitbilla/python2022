#!/usr/bin/env python3
import psutil

process_name = "tmux"
pid = None

for proc in psutil.process_iter():
    if process_name in proc.name():
        pid = proc.pid
        print(f'PID of tmux : {pid}')



"""
from subprocess import check_output
def get_pid(name):
        return int(check_output(["pidof","-s",name]))
get_pid("tmux")
"""
print("####################################################")
for proc in psutil.process_iter(['pid', 'name', 'username']):
    print(proc.info)
