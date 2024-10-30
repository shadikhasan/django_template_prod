from .base import *


SECRET_KEY = os.getenv('SECRET_KEY', 'fallback-secret-key-if-not-found')
DEBUG = True
ALLOWED_HOSTS = ['*']

# Database configuration for development
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Optional: Additional development-specific settings can go here
