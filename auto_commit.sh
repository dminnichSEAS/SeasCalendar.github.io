#!/bin/bash

# Check if booking.txt has been modified
if git diff --quiet booking.txt; then
  exit 0  # No changes, so exit without committing or pushing
fi

# Commit the changes with the message "auto"
git add bookings.txt
git commit -m "auto"

# Push the changes
git push
