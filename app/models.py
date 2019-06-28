
from django.db import models


class Character(models.Model):
    """
        Creating the structure the table "Character" for database
    """
    # character_id = The id is auto generate by
    # SQlite associated with a pimaire key
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    species = models.CharField(max_length=255)
    character_type = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    origin = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    episodes = models.ManyToManyField(Episode, related_name='characters')
    url = models.CharField(max_length=255)
    created = models.CharField(max_length=255)


class Episode(models.Model):
    """
        Creating the structure the table "Episodes" for database
    """
    # episode_id = The id is auto generate by
    # SQlite associated with a pimaire key
    name = models.CharField(max_length=255)
    air_date = models.CharField(max_length=255)
    episode = models.CharField(max_length=255)
    characters = models.ManyToManyField(Character, related_name='episodes')
    url = models.CharField(max_length=255)
    created = models.CharField(max_length=255)


class Location(models.Model):
    """
        Creating the structure the table "Location" for database
    """
    # location_id = The id is auto generate by
    # SQlite associated with a pimaire key
    name = models.CharField(max_length=255)
    location_type = models.CharField(max_length=255)
    dimension = models.CharField(max_length=255)
    residents = models.ManyToManyField(Character, related_name='locations')
    url = models.CharField(max_length=255)
    created = models.CharField(max_length=255)


class Picture(models.Model):
    """
        Creating the associative table of "Character"
        and "Location" for the "Pictures" table
    """
    # picture_id = The id is auto generate by
    # SQlite associated with a pimaire key
    Character_id = models.ForeignKey('characters', on_delete=models.CASCADE)
    Location_id = models.ForeignKey('locations', on_delete=models.CASCADE)
    url = models.CharField(max_length=255)


class Favorite(models.Model):
    """
        Creation of the table "Favorites", to store the
        preferred residents with their rental and type
    """
    # favorite_id = The id is auto generate by
    # SQlite associated with a pimaire key
    resident = models.CharField(max_length=255)
    location_resident = models.CharField(max_length=255)
    type_resident = models.CharField(max_length=255)
    type_location = models.CharField(max_length=255)

    def __str__(self):
        """
            Converted the attribute object
            to string objects
        """
        return self.resident


# pipenv install django-extensions
#
# python manage.py shell

# from app.models import TABLE
#
# fav  = Favorites()
# fav.resident =
# fav.location_resident =
# fav.type_resident =
# fav.type_location =
# fav.save()
#   OR
# fav.objects.create(**attribute='')

### fav.objects.get(pk)
### fav.objects.all() # views method
### fav.objects.filter(pk) # juste return one 'querySet <obj>'
