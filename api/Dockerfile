# Pull official base image
FROM python:3.9.13-buster

# Assign the label for the developer (arbitrary)
LABEL Developer="Mohammad Mahdi Mohajer"

# Set environment variables. These are required for python images
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /usr/src/app

# Update the pip package manager
RUN pip install --upgrade pip

# Copy requirements.txt and install all the required libraries
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy all the files from current folder to --->
# the working directory of the image
COPY . .

# Making the file docker-entrypoint.sh, wait-for executable
RUN chmod +x /usr/src/app/docker-entrypoint-dev.sh
RUN chmod +x /usr/src/app/docker-entrypoint-prod.sh
RUN chmod +x /usr/src/app/wait-for

# Open port 8000, default port for django:
EXPOSE 8000

# Create a user app that belongs to the group app
RUN useradd app

# Change the owner of current folder to the user app --->
# And set the user app as the current user
RUN chown -R app:app .
USER app