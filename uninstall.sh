
#!/bin/bash

REPO_DIR="hellcat"

# Function to uninstall the repository
uninstall_repo() {
    if [ -d "$REPO_DIR" ]; then
        echo "Removing repository..."
        rm -rf "$REPO_DIR"
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
















