#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from Ecommerce_App.settings import base,local


def main():
    """Run administrative tasks."""

    #A TRIGGER TO CHECK WHETHER SETTINGS FILE IS BEING WORKED
    if base.DEBUG:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Ecommerce_App.settings.local')
    else:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Ecommerce_App.settings.production')
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
