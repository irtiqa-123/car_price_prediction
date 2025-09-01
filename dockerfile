# Use official Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . .

# Expose the port your FastAPI app runs on
EXPOSE 8000

# Command to run the app
CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]
