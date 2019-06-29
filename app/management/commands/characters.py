"""
    This file is responsible for collecting all data related to the characters in the series
"""
from django.core.management.base import BaseCommand, CommandError

import requests as req

from pprint import pprint

from app.models import Character


class Command(BaseCommand):
    help = 'Download all characters'

    def handle(self, *args, **kwarg):
        """
            Use the configuration for the connecting interface
        """
        characters = []
        # Go through all the pages
        pages = range(0, 25)
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
            # pprint(characters)
            for character in characters:
                for i in character[:]:
                    test = i['type']
                    # Change the key index in Json response
                    # to avoid word conflicts book
                    i['character_type'] = test
                    del i['type']
                    # import pdb; pdb.set_trace()
                    Character.objects.create(**i)


# python manage.py characters
