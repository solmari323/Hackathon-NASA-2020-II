from django.db import models


class Schedule(models.Model):
    title = models.CharField(max_length=200)
