#!/bin/bash

# Check if the file with URLs is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <file_with_urls>"
  exit 1
fi

# Read the file line by line
while IFS= read -r url
do
  # Run the sqlmap command for each URL
  sqlmap -u "$url" --dbs
done < "$1"

