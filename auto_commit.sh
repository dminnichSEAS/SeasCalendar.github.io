#!/bin/bash

# Set your GitHub repository URL
REPO_URL="https://github.com/dminnichSEAS/SeasCalendar.github.io.git"

# Directory containing your Git repository
REPO_DIR="/workspaces/SeasCalendar.github.io"

# Check if bookings.txt is modified
if git -C "$REPO_DIR" status --porcelain | grep -q "bookings.txt"; then
    # Commit the changes
    git -C "$REPO_DIR" add bookings.txt
    git -C "$REPO_DIR" commit -m "Automatic commit for modified bookings.txt"

    # Push the changes to the remote repository
    git -C "$REPO_DIR" push origin master  # Change 'master' to your branch name if needed
    echo "Changes committed and pushed to the repository."
else
    echo "No modifications in bookings.txt."
fi
