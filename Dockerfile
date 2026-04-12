FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (for caching)
COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy full project
COPY . .

# Create non-root user
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

# 👇 IMPORTANT: ADK runs inside agents folder
WORKDIR /app/agents

# Expose ADK web port
EXPOSE 8000

# 👇 Run ADK Web UI
CMD ["adk", "web", "--host", "0.0.0.0", "--port", "8000"]