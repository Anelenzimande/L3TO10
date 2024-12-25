# Use Python 3.13 when officially available (or use a stable version like 3.12)
FROM python:3.13-slim   

WORKDIR /app
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Command to run your Django app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

