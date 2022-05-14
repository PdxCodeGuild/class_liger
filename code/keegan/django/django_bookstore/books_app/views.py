from django.shortcuts import render, redirect

from .models import Author, Book, Genre

def index(request):

    books = Book.objects.all()

    context = {
        'books': books
    }

    return render(request, 'index.html', context)


def add_book(request):
    form = request.POST

    author_name = form.get('author')
    book_title = form.get('title')
    genre_titles = form.get('genres').split(' ')

    # get the author from the database if it exists,
    # otherwise create it
    # .get_or_create returns a tuple, (obj:ModelInstance, created:bool)
    # 'unpack' the tuple into two variables
    author, created = Author.objects.get_or_create(name=author_name)

    # create a book instance with the author that was just gotten or created
    book = Book.objects.create(title=book_title, author=author)


    # loop through the genre titles
    # get or create each and add them to the books genres
    for genre_title in genre_titles:
        genre, created = Genre.objects.get_or_create(title=genre_title)

        # add the gotten or created genre to the book's genres list
        book.genres.add(genre)



    return redirect('books_app:index')