from django.contrib import admin

from app.models import Location, Episode, Character, Favorite


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass

@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    pass

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    pass

@admin.register(Favorite)
class EpisodeAdmin(admin.ModelAdmin):
    pass

