#!/bin/bash

# Define the repository URL
REPO_URL="https://github.com/strangedreamer4/hellcat.git"
REPO_DIR="hellcat"

# Navigate to the parent directory
cd ..

# Remove the old repository directory
if [ -d "$REPO_DIR" ]; then
    echo "Removing previous repository..."
    rm -rf "$REPO_DIR"
fi

# Clone the new repository
echo "Cloning repository..."
git clone "$REPO_URL" "$REPO_DIR"

echo "Update complete!"
