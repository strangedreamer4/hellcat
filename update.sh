#!/bin/bash

# Define the repository URL
REPO_URL="https://github.com/strangedreamer4/hellcat.git"

# Define a function to update the repository
update_repo() {
    # Check if the repository directory already exists
    if [ -d "hellcat" ]; then
        if [ -d "hellcat/.git" ]; then
            echo "Updating repository..."
            cd hellcat
            git pull origin main
            cd ..
        else
            echo "The 'hellcat' directory exists but is not a Git repository."
            echo "Please manually remove or backup the directory and re-run the script."
        fi
    else
        echo "Cloning repository..."
        git clone "$REPO_URL" hellcat
    fi
}

# Run the update_repo function
update_repo

echo "Update complete!"
