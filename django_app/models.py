from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=50, unique=True)
    author = models.CharField(max_length=50, null=True)
    volume = models.IntegerField(null=True)

    def __str__(self):
        return "{} - {}, vol: {}\n".format(self.title, self.author, self.volume)


class AsyncBook(models.Model):
    title = models.CharField(max_length=50, unique=True)
    author = models.CharField(max_length=50, null=True)
    volume = models.IntegerField(null=True)

    def __str__(self):
        return "{} - {}, vol: {}\n".format(self.title, self.author, self.volume)
