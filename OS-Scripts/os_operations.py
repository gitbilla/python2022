#!/usr/bin/env python3
try:
    import os, sys, time, re
    from pprint import pprint as pp
    from subprocess import check_output
    import psutil
    print('imported all the modules')
except ModuleNotFoundError:
        print('Install the Module')
        sys.exit(1)
print('The Number of CPUS:', psutil.cpu_count())
load_cpu = psutil.getloadavg()
print(f'CPU Load : {load_cpu}')
load_cpu_per =  [x / psutil.cpu_count() * 100 for x in psutil.getloadavg()]
print(f'CPU Load in Percentage : {load_cpu_per}')

# MEMORY
print('RAM memory % used:', psutil.virtual_memory()[2])

# Top 3 process consuming
pp([(p.pid, p.info['name'], sum(p.info['cpu_times'])) for p in sorted(psutil.process_iter(['name', 'cpu_times']), key=lambda p: sum(p.info['cpu_times'][:2]))][-3:])

# Processes consuming more than 500M of memory:
print('Process consuming mor than 500M of Memory')
pp([(p.pid, p.info['name'], p.info['memory_info'].rss) for p in psutil.process_iter(['name', 'memory_info']) if p.info['memory_info'].rss > 200 * 1024 * 1024])


 
# Iterate over Generator object to get 
# each process object contained by it
