# Use the official Python image as a parent image
FROM python:3.10-slim

# Install Poetry
RUN pip install poetry

# Set the working directory
WORKDIR /app

# Copy the poetry files for dependencies
COPY ["pyproject.toml", "poetry.lock", "./"]

# Install dependencies with Poetry
RUN poetry install --only main

# Copy the API and predictionModel files
COPY ["./src", "./src"]

# Expose the port your FastAPI app will run on
EXPOSE 9696

# Set the entry point to run your FastAPI app
ENTRYPOINT ["poetry", "run", "uvicorn", "src.API.main:app", "--host", "0.0.0.0", "--port", "9696","--reload"]

