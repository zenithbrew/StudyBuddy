import os
from django.core.management.utils import get_random_secret_key

def update_secret_key(settings_path='studybud/settings.py'):
    new_secret_key = get_random_secret_key()
    secret_key_line = f"SECRET_KEY = '{new_secret_key}'\n"
    with open(settings_path, 'r') as file:
        lines = file.readlines()
    
    with open(settings_path, 'w') as file:
        for line in lines:
            if line.startswith('SECRET_KEY'):
                file.write(secret_key_line)
            else:
                file.write(line)

if __name__ == "__main__":
    update_secret_key()

