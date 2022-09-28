from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=50, null=True)
    description = models.TextField()
    is_active = models.BooleanField()
    is_home = models.BooleanField(default=False)

class Category(models.Model):
    name = models.CharField(max_length=155)
