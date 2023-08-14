#!/bin/bash

# Define the repository URL
REPO_URL="https://github.com/strangedreamer4/hellcat.git"
REPO_DIR="hellcat"

# Function to update the repository
update_repo() {
    if [ -d "$REPO_DIR" ]; then
        echo "Removing previous repository..."
        rm -rf "$REPO_DIR"
    fi

    echo "Cloning repository..."
    git clone "$REPO_URL" "$REPO_DIR"
}

# Run the update_repo function
update_repo

echo "Update complete!"
