from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(
        max_length=70,
        help_text="Title of the book",
        null=False,
        default="Title")
    contributors = models.TextField(
        max_length=200)
    publisher = models.CharField(
        default="publisher",
        max_length=50)
