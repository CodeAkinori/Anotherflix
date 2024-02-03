from django.db import models
from django.urls import reverse
class Game(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    platform = models.CharField(max_length=50)
    image_url = models.URLField()

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'games'
        managed = True
        verbose_name = 'game'
        verbose_name_plural = 'games'
    
    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})
    
