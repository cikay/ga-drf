from django.db import models

# Create your models here.


class Author(models.Model):

    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
