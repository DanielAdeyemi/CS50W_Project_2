from unicodedata import category
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Comment(models.Model):
    comment = models.TextField()

    def __str__(self):
        return f"{self.comment}"


class Bid(models.Model):
    initial_bid = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return f"{self.initial_bid}"


class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    picture = models.URLField()
    creation_time = models.DateTimeField(auto_now_add=True)
    current_bid = models.ForeignKey(
        Bid, on_delete=models.CASCADE, related_name='bid')
    comments = models.ForeignKey(
        Comment, on_delete=models.CASCADE, related_name='comments')
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='creator')
    category = models.TextField()
