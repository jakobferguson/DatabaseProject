#!/bin/bash

# Check if SQLite3 is installed
if ! command -v sqlite3 &> /dev/null
then
    echo "sqlite3 could not be found, please install it first."
    exit 1
fi

# Execute the SQL commands to create the database
sqlite3 tuple.db < workOutGen.sql

echo "Database created and initialized successfully."

python3 GUI.py