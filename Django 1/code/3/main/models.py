from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=100)
    predators = models.CharField(max_length=100)
    num_restaurants = models.IntegerField(max_digits=3)
    img_url = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
