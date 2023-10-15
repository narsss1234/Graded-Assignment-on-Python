# Write a Python program to monitor the health of the CPU.

# import psutil

import psutil

print("Monitoring CPU usage...")

# Using while block so that the program keeps running until interrupted

while True:
    # try block to fetch the cpu_percentage and display
    try:
        # storing the cpu_percentage, which is obtained in 2 seconds time
        cpu_percentage = psutil.cpu_percent(2)
        print("The current CPU usage percent is: ", cpu_percentage)

        # if block to alert user, when the cpu usage hits threshold
        if cpu_percentage >=80:
            print("Alert! CPU usage is exceeding threshold!!!!")
        else:
            continue
    # exception handling
    except KeyboardInterrupt:
        print("The health check program was interrupted manually.")
        break