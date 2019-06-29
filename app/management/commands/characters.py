from django.core.management.base import BaseCommand, CommandError

import requests as req

from app.models import Character


class Command(BaseCommand):
    help = 'Download all characters'

    def handle(self, *args, **options):
        """
            Use the configuration for the connecting interface
        """
        characters = []
        pages = [0, 1, 2, 3, 4]
        # Address  rick and morty api the API
        url = "https://rickandmortyapi.com/api/character/"
        # This config for connecting API
        for count in pages:
            config = {"action": "process",
                      # All the content of the page
                      "tag_contains_0": "contains",
                      # Go through all the pages to collect all the data
                      "page": count,
                      # Return the format
                      "json": 1,
                      }
            # Use GET method for the request
            response = req.get(url, params=config)
            # Use the Json response
            results = response.json()
            # select the desired content
            characters.append(results['results'])
            for character in characters:
                Character.objects.create(**character)


# python manage.py characters
