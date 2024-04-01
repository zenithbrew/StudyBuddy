FROM python:3.12

# Set the working directory in the container
WORKDIR /app

RUN apt-get update && \
    apt-get install -y git

ARG GIT_REPO_URL
ARG GIT_BRANCH=main
RUN git clone --branch $GIT_BRANCH $GIT_REPO_URL .


# Install dependencies
RUN pip install --no-cache-dir -r ./requirements.txt

ENV SECRET_KEY='3#av2c6nptlbbb6^muqkch37rtuef83@+g$v!ir-f5%doocb43q@#$@$dsf#!3Daf1313Djhkk###'
ENV EMAIL_HOST_USER='email_here'
ENV EMAIL_HOST_PASSWORD='password_here'
# Expose the port on which the Django app will run
EXPOSE 8000

# Run the Django app
CMD ["python", "studybud/manage.py", "runserver", "0.0.0.0:8000"]