from django.db import models
from django.contrib.gis.db import models

# Create your models here.
class Pits(models.Model):
    Comment = models.CharField(max_length=100)
    Coords = models.PointField(srid=4326, null=True)

    def __str__(self):
        return self.Comment
    
    class Meta:
        verbose_name_plural = 'Pits'

class Bulbs(models.Model):
    Comment = models.CharField(max_length=100)
    Coords = models.PointField(srid=4326, null=True)

    def __str__(self):
        return self.Comment
    
    class Meta:
        verbose_name_plural = 'Bulbs'

class Leaks(models.Model):
    Comment = models.CharField(max_length=100)
    Coords = models.PointField(srid=4326, null=True)

    def __str__(self):
        return self.Comment
    
    class Meta:
        verbose_name_plural = 'Leaks'