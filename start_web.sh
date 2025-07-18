#!/bin/bash
echo "Starting Python Calculator Web Application..."
echo "Installing dependencies..."
pip3 install --break-system-packages -r requirements.txt

echo "Starting Flask server..."
python3 app.py