"""
WSGI config for {{ petor.project.name }} project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
import sys
import environ
from pathlib import Path
from django.core.wsgi import get_wsgi_application

env = environ.Env()

BASE_DIR = Path(__file__).parent.parent
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

sys.path.append(str(BASE_DIR / "src"))

if os.environ.get('DJANGO_ENV') == 'production':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.production')
elif os.environ.get('DJANGO_ENV') == 'local':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')
else:
    print("DJANGO_ENV is not set")
    sys.exit(1)

application = get_wsgi_application()
