#!/bin/bash

# Check if booking.txt has changed
if git diff --quiet booking.txt; then
    exit 0
fi

# Commit and push changes
git add booking.txt
git commit -m "Auto-commit: Update booking.txt"
git push origin <branch_name>
