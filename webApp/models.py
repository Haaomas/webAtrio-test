from django.db import models

# Create your models here.


class Person(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    birth_date = models.DateField()

    def __str__(self):
        return self.firstname
