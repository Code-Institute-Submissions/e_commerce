from django.db import models
from django.utils import timezone

class Repair(models.Model):

    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to="images", blank=True, null=True)
    
    def __str__(self):
        return self.title