from django.shortcuts import render

from django.db import connection, reset_queries

from .models import User, BlogPost, Comment


def index(request):


    # retrieve only the users, not their blogposts or the blogposts' comments
    # 1102 queries to get all the blog posts and comments
    # users = User.objects.all()

    # retrieve the users and all of their blogposts, but not the blogposts' comments
    # 1002 queries instead of 1102
    # users = User.objects.all().prefetch_related('blogposts')

    # retrieve the users, all of their blogposts, and all the comments
    # 3 queries!
    users = User.objects.all().prefetch_related('blogposts__comments')


    # print(users.last()) # 1 query
    # print(users.last().blogposts.first().comments.first()) # 3 queries

    for user in users:
        pass
        for blogpost in user.blogposts.all():
            pass
            for comment in blogpost.comments.all():
                pass

    query_count = len(connection.queries)


    context = {
        'query_count': query_count,
        'users': users
    }

    return render(request, 'index.html', context)
