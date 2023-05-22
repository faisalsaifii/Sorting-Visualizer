from django.db import models


class SortingAlgorithm(models.Model):
    name = models.CharField(max_length=100)
    numbers = models.CharField(max_length=1000)
