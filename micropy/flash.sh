#!/bin/bash

# BASH SCRIPT TO AUTOMATE UPLOADING TO THE ESP8266
# By Roy Medina

# Set python PATH
PATH=~/.local/bin:$PATH

# Set the serial port
PORT="/dev/ttyUSB0"

# Get permissions to write to the PORT
sudo chmod 666 "$PORT"

# Get the list of .py files in the current directory
# FILES=$(find . -type f -name "*.py")
#ADD modelo_neuronal.pkl
FILES= "reto_ml.py"
# FILES+=" modelo_neuronal.joblib"
# FILES+="sensor_tempp.py"
FILES+="SensorDHT.py"
# Iterate over each file and upload it
for file in $FILES; do
    echo "Uploading $file..."
    ampy -p "$PORT" put "$file"
done

echo "Upload complete!"

# Enter REPL
picocom "$PORT" -b115200

