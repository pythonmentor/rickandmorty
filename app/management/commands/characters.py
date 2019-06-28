from django.core.management.base import BaseCommand, CommandError

import requests as req

from app.models import Character


class Command(BaseCommand):
    help = 'Dowload all characters'

    def handle(self, *args, **options):
        """
            Use the configuration for the connecting interface
        """
        characters = []
        # Address  rick and morty api the API
        location = "https://rickandmortyapi.com/api/character/"
        # This config for connecting API
        config = {"action": "process",
                  # All the content of the page
                  "tag_contains_0": "contains",
                  # Count pages
                  "page": 1,
                  # Return the format
                  "json": 1,
                  }
        # Use GET method for the request
        response = req.get(location, params=config)
        # Use the Json response
        results = response.json()
        characters.append(results)
        for character in characters:
            Character.objects.create(**character)


# python manage.py characters
