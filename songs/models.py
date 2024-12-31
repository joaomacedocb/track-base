from django.db import models
from uuid import uuid4

class Genre(models.Model):
    id = models.UUIDField(primary_key=True, default= uuid4, editable=False)
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name

class Song(models.Model):
    id_song = models.UUIDField(primary_key=True, default= uuid4, editable=False)
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    duration = models.DurationField()
    record = models.CharField(max_length=100)
    genres = models.ManyToManyField(Genre, related_name="songs")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.name} by {self.artist}'
    
