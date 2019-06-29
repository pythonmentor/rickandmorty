from django.core.management.base import BaseCommand, CommandError

import requests as req

from app.models import Picture


class Command(BaseCommand):
    help = 'Download all episodes'

    def handle(self, *args, **options):
        """ Use the configuration for the connecting interface """
        pictures = []
        # Address  rick and morty api the API
        url = "https://rickandmortyapi.com/api/episode/"
            # This config for connecting API
        config = {
                       "action": "process",
                       "tag_contains_0": "contains",    # All the content of the page
                       "page": 1,                       # Count pages
                       "json": 1 }                      # Return the format
        response = req.get(url , params=config)    # Use GET method for the request
        results = response.json()                    # Use the Json response
        pictures.append(results) # results['results']
        for picture in pictures:
            Picture.objects.create(**picture)


# python manage.py episodes