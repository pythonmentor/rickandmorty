"""
    This file is responsible for collecting all data related to the episodes of the series
"""
from django.core.management.base import BaseCommand, CommandError

import requests as req

from app.models import Episode


class Command(BaseCommand):
    help = 'Download all episodes'

    def handle(self, *args, **options):
        """
            Use the configuration for the connecting interface
        """
        episodes = []
        # Go through all the pages
        pages = range(0, 2)
        # Address  rick and morty api the API
        url = "https://rickandmortyapi.com/api/episode/"
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
            episodes.append(results['results'])
            # pprint(characters)
            for episode in episodes:
                for i in episode:
                    # import pdb; pdb.set_trace()
                    Episode.objects.create(**i)


# python manage.py episodes
