#!/bin/bash

# Define the repository name
REPO_NAME="hellcat"

# Function to uninstall the repository
uninstall_repo() {
    # Find the absolute path of the repository directory
    REPO_DIR=$(find ~ -type d -name "$REPO_NAME" -print -quit 2>/dev/null)

    if [ -n "$REPO_DIR" ]; then
        echo "Removing repository..."
        rm -rf "$REPO_DIR"
        echo "Repository removed."
    else
        echo "Repository directory not found."
    fi
}

# Run the uninstall_repo function
uninstall_repo
sleep 2
pip uninstall -y tk
pip uninstall -y Pillow
pip uninstall -y pyrebase4
clear
echo "Uninstall complete!"
















