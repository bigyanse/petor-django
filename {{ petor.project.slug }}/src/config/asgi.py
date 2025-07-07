"""
ASGI config for {{ petor.project.name }} project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os
import sys
from pathlib import Path

from django.core.asgi import get_asgi_application

BASE_DIR = Path(__file__).parent.parent.parent
sys.path.append(str(BASE_DIR / "src/apps"))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.config.settings.local')

application = get_asgi_application()
