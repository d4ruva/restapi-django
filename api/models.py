from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=50)
    division = models.CharField(max_length=5)
    standard = models.IntegerField()

    def __str__(self):
        return self.name
