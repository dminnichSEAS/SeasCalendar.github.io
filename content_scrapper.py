#Retrieved the data from other repo bookings.txt and puts it into this this
# Run with --> python content_scrapper.py


import os
import shutil
import time

file1 = 'C:/Users/seas/Desktop/TSv3-main/bookings.txt'
file2 = 'C:/Users/seas/Desktop/CalendarRepoClone/SeasCalendar.github.io/bookings.txt'

while True:
    shutil.copy2(file1, file2)
    # Get the last modification time of both files
    file1_mtime = os.path.getmtime(file1)
    file2_mtime = os.path.getmtime(file2)

    # Check if file1 is different from file2 (based on modification time)
    if file1_mtime > file2_mtime:
        print(f"{file1} is different from {file2}. Updating {file2}...")
        shutil.copy2(file1, file2)
    elif file1_mtime < file2_mtime:
        print(f"{file2} is different from {file1}. Updating {file1}...")
        shutil.copy2(file2, file1)
    else:
        print(f"{file1} and {file2} are the same.")

    # Wait for 20 seconds before checking again
    time.sleep(3)
