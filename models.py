from django.db import models
from django.urls import reverse

class movies1(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    desc=models.CharField(max_length=500)
    year=models.IntegerField()
    genre=models.CharField(max_length=50)
   
    def get_absolute_url(self):
        return reverse('list')