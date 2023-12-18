# run with --> python auto_commit_local.py
import os
import subprocess
import time

# Define the repository path
repo_path = 'C:/Users/seas/Desktop/CalendarRepoClone/SeasCalendar.github.io'

# Define the file to monitor for changes
file_to_monitor = 'bookings.txt'

def is_file_modified(file_path):
    # Check if the file has been modified
    try:
        output = subprocess.check_output(['git', 'status', '--porcelain', file_path], cwd=repo_path).decode('utf-8')
        return not output.startswith("??")  # Check if it's not an untracked file
    except subprocess.CalledProcessError:
        return False
  
def git_commit_and_push(file_path):
    # Commit and push changes in the specified file
    subprocess.call(['git', 'add', file_path], cwd=repo_path)
    subprocess.call(['git', 'commit', '-m', 'Auto commit for ' + file_path], cwd=repo_path)
    subprocess.call(['git', 'push'], cwd=repo_path)

def main():
    # Set the working directory
    os.chdir(repo_path)

    while True: 
        # Open the source file in read mode
        with open('C:/Users/seas\Desktop/TSv3-main/bookings.txt', 'r') as source_file:
    # Read the content
            content = source_file.read()

# Open the destination file in append mode
            with open('bookings.txt', 'w') as destination_file:
    # Write the content
                destination_file.write(content)

        # Check if the specified file has been modified
        if is_file_modified(file_to_monitor):
            print(f"Changes detected in {file_to_monitor}. Committing and pushing...")
            git_commit_and_push(file_to_monitor)
            print(f"Changes in {file_to_monitor} have been committed and pushed.")
        else:
            print(f"No changes in {file_to_monitor}.")

        # Wait for a certain interval before checking again (e.g., every 60 seconds)
        time.sleep(100)


if __name__ == '__main__':
    main()
