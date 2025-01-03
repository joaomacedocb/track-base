from django.db import models
from uuid import uuid4

class Artist(models.Model):
    id = models.UUIDField(primary_key=True, default= uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    bio = models.TextField(max_length=500)
    photo = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name