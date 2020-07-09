from django.db import models
from datetime import datetime


class Story(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField(default=datetime.now, blank=True)
    body = models.TextField()
    image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title