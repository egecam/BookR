from django.db import models
import datetime as dt

# Create your models here.


class Contributor(models.Model):
    name = models.CharField(max_length=40, help_text="First name")
    surname = models.CharField(
        max_length=50, help_text="Last name")


class Book(models.Model):
    title = models.CharField(
        max_length=70,
        help_text="Title of the book",
        null=False,
        default="Title")
    contributors = models.ManyToManyRel(
        to='Contributor', through='BookContributor')
    publisher = models.models.ForeignKey(
        'Publisher',
        on_delete=models.SET_DEFAULT,
        release_date=models.DateField(default=dt.date[2023, 3, 9]),
        default="default value")
    isbn = models.IntegerField(
        help_text="ISBN of the book",
        unique=True)

    def __str__(self):
        return "Book:"+self.title+"isbn:"+self.isbn


class Publisher(models.Model):
    name = models.CharField(
        max_length=50, help_text="Name of the publisher")
    email = models.EmailField(help_text="email address")
    website = models.URLField(help_text="website address")

    def __str__(self):
        return "Publisher info:"+self.name+"\n"
        +self.email+"\n"
        +self.website


class BookContributor(models.Model):
    # Enumerated Type
    class ContributorRole(models.TextChoices):
        AUTHOR = "AUTHOR", "Author"
        CO_AUTHOR = "CO_AUTHOR", "Co-Author"
        EDITOR = "EDITOR", "Editor"

    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    contributor = models.ForeignKey(
        'Contributor', on_delete=models.CASCADE)
    role = models.CharField(
        max_length=20, choices=ContributorRole.choices)
