from django.db import models

# Create your models here.
class Notes(models.Model):
    chapter = models.IntegerField()
    notes = models.TextField()
    marks = models.IntegerField()
    new_check = models.IntegerField(default=0)