#!/bin/sh

# Run the flask app in the background
echo "Starting Flask app"
python3 -m flask run --host=0.0.0.0 --port=5000 &

# Sleep for a moment to ensure the Flask app has started
sleep 5

# Initiate the database
echo "Initiating the database"
python3 -m flask init-db

echo "Database initiated"

# Keep the container running
tail -f /dev/null