from .base import *

# Testing settings
DEBUG = False
ALLOWED_HOSTS = ['testserver']

# Use an in-memory database for testing
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

# Test-specific configurations
