# Use the official Python image as a parent image
FROM python:3.10-slim

# Install pipenv
RUN pip install pipenv

# Set the working directory
WORKDIR /app

# Copy Pipfiles for dependencies
COPY ["Pipfile", "Pipfile.lock", "./"]

# Install dependencies with pipenv
RUN pipenv install --deploy --system

# Copy the API and predictionModel files

COPY ["./src", "./src"]

# Expose the port your FastAPI app will run on
EXPOSE 9696

# Set the entry point to run your FastAPI app
ENTRYPOINT ["pipenv", "run", "uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "9696","--reload"]

