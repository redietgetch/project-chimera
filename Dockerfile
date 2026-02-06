# Dockerfile for Project Chimera
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . /app

# Install Python dependencies (if using pyproject.toml or requirements.txt)
RUN pip install --upgrade pip
RUN if [ -f pyproject.toml ]; then pip install .; elif [ -f requirements.txt ]; then pip install -r requirements.txt; fi

CMD ["bash"]
