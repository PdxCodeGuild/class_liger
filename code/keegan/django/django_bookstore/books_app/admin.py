from django.contrib import admin
from .models import Author, Book, Genre

# create an inline to views the many-to-many relationship between books and genres
class GenreInline(admin.TabularInline):
    model = Genre.books.through

# customize the look and included fields of the book admin page
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']
    inlines = [GenreInline]



admin.site.register(Book, BookAdmin)


# for the models to show in the admin panel
admin.site.register([Author, Genre])