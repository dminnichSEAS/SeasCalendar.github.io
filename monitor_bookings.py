#  chmod +x auto_commit.sh
#  chmod +x monitor_bookings.py


import os
import time
import subprocess

file_to_watch = "bookings.txt"

while True:
    timestamp = os.path.getmtime(file_to_watch)
    try:
        last_timestamp
    except NameError:
        last_timestamp = timestamp

    if timestamp != last_timestamp:
        subprocess.run(["/bin/bash", "auto_commit.sh"])
        last_timestamp = timestamp

    time.sleep(1)  # Adjust the interval as needed
