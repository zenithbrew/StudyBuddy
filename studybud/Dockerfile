FROM python:3.12

# Set the working directory in the container
WORKDIR /app

COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r ./requirements.txt

# Expose the port on which the Django app will run
EXPOSE 8000

# Run the Django app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]