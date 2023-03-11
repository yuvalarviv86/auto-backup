import os
import shutil
import time
from datetime import datetime, timedelta

# Get the file path from the user
file_path = input("Enter the path of the file to backup: ")

# Get the backup location from the user
backup_path = input("Enter the path of the backup location: ")

# Get the frequency of backups from the user
while True:
    backup_frequency = input("Enter the frequency of backups (hours, days, or months): ")
    if backup_frequency not in ["hours", "days", "months"]:
        print("Invalid frequency entered. Please enter 'hours', 'days', or 'months'.")
    else:
        break

# Get the interval between backups based on the selected frequency
if backup_frequency == "hours":
    while True:
        try:
            backup_interval = int(input("Enter the number of hours between backups: "))
            backup_interval = timedelta(hours=backup_interval)
            break
        except ValueError:
            print("Invalid input entered. Please enter a positive integer.")
elif backup_frequency == "days":
    while True:
        try:
            backup_interval = int(input("Enter the number of days between backups: "))
            backup_interval = timedelta(days=backup_interval)
            break
        except ValueError:
            print("Invalid input entered. Please enter a positive integer.")
elif backup_frequency == "months":
    while True:
        try:
            backup_interval = int(input("Enter the number of months between backups: "))
            backup_interval = timedelta(days=backup_interval * 30)
            break
        except ValueError:
            print("Invalid input entered. Please enter a positive integer.")

# Set the initial backup time
next_backup_time = datetime.now() + backup_interval

# Show a green message indicating that the program is now running
print("\033[92mBackup program is now running...")

# Continuously check the time and initiate backups when necessary
while True:
    current_time = datetime.now()
    if current_time >= next_backup_time:
        # Copy the file to the backup location
        backup_file_path = os.path.join(backup_path, os.path.basename(file_path))
        shutil.copyfile(file_path, backup_file_path)

        # Update the next backup time
        next_backup_time = current_time + backup_interval

        print("Backup successful at", current_time)

    # Pause the program for 10 seconds before checking the time again
    time.sleep(10)
