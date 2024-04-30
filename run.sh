#!/bin/bash

# Check if SQLite3 is installed
if ! command -v python3 &> /dev/null
then
    echo "python3 could not be found, please install it first."
    sudo apt-get update
    sudo apt-get install -y python3
fi
if ! command -v sqlite3 &> /dev/null
then
    echo "sqlite3 could not be found, please install it first."
    sudo apt-get update
    sudo apt-get install -y sqlite3
fi
python3 check_dependencies.py
# Execute the SQL commands to create the database
sqlite3 tuple.db < workOutGen.sql

echo "Database created and initialized successfully."

python3 GUI.py