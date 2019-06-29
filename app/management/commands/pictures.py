"""
    This file has for responsibility to collect all the images
    related to the characters and the planets of the series
"""
from django.core.management.base import BaseCommand, CommandError

import requests as req

from app.models import Picture


class Command(BaseCommand):
    help = 'Download all episodes'

    def handle(self, *args, **options):
        """

        """
        pass


# python manage.py # python manage.py commands.file