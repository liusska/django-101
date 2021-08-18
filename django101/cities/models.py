from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    home_town = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.name}'
