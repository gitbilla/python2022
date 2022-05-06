#!/usr/bin/env python3
try:
    import sys, os, time
    import psutil
    print('Module is imported')
except ModuleNotFoundError:
    print('Install the Module')
    sys.exit(1)



# Calling psutil.cpu_precent() for 4 seconds
count = 1
while count < 5:
    print('The CPU usage is: ', psutil.cpu_percent(4))
    print('RAM memory % used:', psutil.virtual_memory()[2])
    print("Completed the cycle")
    time.sleep(2)
    count += 1


# Getting all memory using os.popen()
total_memory, used_memory, free_memory = map(
            int, os.popen('free -t -m').readlines()[-1].split()[1:])

# Memory usage
print("RAM memory % used:", round((used_memory/total_memory) * 100, 2))
