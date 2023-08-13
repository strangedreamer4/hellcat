#!/bin/bash

# Uninstall dependencies
echo "Uninstalling dependencies..."
sleep 2
pip uninstall -y tk
pip uninstall -y Pillow
pip uninstall -y pyrebase4
clear
# Remove the app
echo "Removing the app..."
sleep 2
cd ..
rm -rf hellcat 
clear
echo "Uninstallation completed."
sleep 2
exit 
