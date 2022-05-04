from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)

    # associate an author with the book
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


    def __str__(self):
        return self.title


class Genre(models.Model):
    title = models.CharField(max_length=255)

    # allow each genre to be related to multiple books and 
    # each book to be related to multiple genres
    books = models.ManyToManyField(Book, related_name='genres')

    def __str__(self):
        return self.title