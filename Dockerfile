# Dockerfile for the flask app
FROM python:3.11-alpine

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000:5000

# Define environment variable for flask app
ENV FLASK_APP="todo"

# Create a script to run the flask app and initialize the database and run it
RUN chmod +x entrypoint.sh

# Run the script as the entrypoint when the container launches
ENTRYPOINT ["./entrypoint.sh"]

# Normally, the flask app would be run with the following command, but in this case
# we are using the entrypoint script to run the flask app and initialize the database
# because the database is not initialized when the flask app is run
# CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]


