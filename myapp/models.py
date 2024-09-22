from django.db import models

class ExampleModel(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()