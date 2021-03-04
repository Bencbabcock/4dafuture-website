from django.db import models
from django.utils import timezone

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField(default=timezone.now)
    url = models.URLField(blank=True)
    image = models.ImageField(upload_to='blog/images/', null=True)

    def __str__(self):
        return self.title
