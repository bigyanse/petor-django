#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import environ
from pathlib import Path

env = environ.Env()

BASE_DIR = Path(__file__).parent

environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

def main():
    """Run administrative tasks."""
    if os.environ.get('DJANGO_ENV') == 'production':
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.production')
    elif os.environ.get('DJANGO_ENV') == 'local':
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')
    else:
        print("DJANGO_ENV is not set")
        sys.exit(1)

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    BASE_DIR = Path(__file__).parent
    sys.path.append(str(BASE_DIR / "src"))

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
