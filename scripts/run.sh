#!/bin/bash

# This script runs the compiled simulation program

# Check if the configuration file is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <config_file.json>"
    exit 1
fi

CONFIG_FILE=$1

# Run the simulation program with the provided configuration file
./build/simulation_program $CONFIG_FILE