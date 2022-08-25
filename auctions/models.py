from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Comment(models.Model):
    comments = models.CharField()

    def __str__(self):
        return f"{self.comments}"


class Bid(models.Model):
    initial_bid = models.DecimalField(decimal_places=2)

    def __str__(self):
        return f"{self.initial_bid}"


class Listing(models.Model):
    pass
