"""
    This file is responsible for collecting all data related to the locations of the series
"""
from django.core.management.base import BaseCommand, CommandError

import requests as req

from app.models import Location


class Command(BaseCommand):
    help = 'Download all locations'

    def handle(self, *args, **options):
        """
            Use the configuration for the connecting interface
        """
        locations = []
        # Go through all the pages
        pages = range(0, 4)
        # Address  rick and morty api the API
        url = "https://rickandmortyapi.com/api/location/"
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
            locations.append(results['results'])
            for location in locations:
                for i in location:
                    test = i['type']
                    # Change the key index in Json response
                    # to avoid word conflicts book
                    i['location_type'] = test
                    del i['type']

                    # import pdb; pdb.set_trace()
                    Location.objects.create(**location)


# python manage.py locations