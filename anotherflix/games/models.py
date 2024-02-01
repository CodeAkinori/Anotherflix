from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    platform = models.CharField(max_length=50)
    image_url = models.URLField()

    def __str__(self):
        return self.name
