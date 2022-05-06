#!/usr/bin/env python3
try:
    import os, sys, time
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
mem = psutil.virtual_memory()
print(mem)

# DISKS
disk = psutil.disk_partitions()
print(disk)
#psutil.disk_usage('/')

#
#Process consuming

for p in psutil.process_iter(['name', 'open_files']):
    for file in p.info['open_files'] or []:
        if file.path.endswith('.log'):
            print("%-5s %-10s %s" % (p.pid, p.info['name'][:10], file.path))


# Top 3 process consuming
pp([(p.pid, p.info['name'], sum(p.info['cpu_times'])) for p in sorted(psutil.process_iter(['name', 'cpu_times']), key=lambda p: sum(p.info['cpu_times'][:2]))][-3:])

# Processes consuming more than 500M of memory:
pp([(p.pid, p.info['name'], p.info['memory_info'].rss) for p in psutil.process_iter(['name', 'memory_info']) if p.info['memory_info'].rss > 500 * 1024 * 1024])

#pid of processes by name
name = 'tmux'
def get_pid(name):
    return check_output(["pidof",name])
    print('tmux pid')
get_pid('tmux')
print('END')


"""


def main():
    count = 1
    while count < 5:
            print('The CPU usage is: ', psutil.cpu_percent(4))
            print('RAM memory % used:', psutil.virtual_memory()[2])
            print("Completed the cycle")
            time.sleep(1)
           # _=os.system("clear")
            count += 1
            #time.sleep(2)


if __name__ == '__main__':
    main()
    _=os.system("clear")
    main()
    #time.sleep(2)
"""
