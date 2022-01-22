from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=250)
    phone = models.CharField(max_length=10)
    email = models.TextField(blank=True)

    def __str__(self):
        return self.name

# Create your models here.