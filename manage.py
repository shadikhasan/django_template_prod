#!/usr/bin/env python
import os
import sys
from pathlib import Path

def main():
    # Define the settings module based on DJANGO_ENV
    DJANGO_ENV = os.getenv('DJANGO_ENV', 'dev')
    
    print(DJANGO_ENV)
    
    # Map DJANGO_ENV to the appropriate settings module
    settings_module = {
        'prod': 'core.settings.prod',
        'test': 'core.settings.test',
        'dev': 'core.settings.dev'
    }.get(DJANGO_ENV, 'core.settings.dev')  # Default to 'dev' if DJANGO_ENV is not found

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
