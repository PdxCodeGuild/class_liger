from django.core.management.base import BaseCommand
import requests

from n_plus_one_app.models import *

def split_name(name):
    '''Split the full name from the API JSON into a first and last name, handling two three-part names'''
    match name:
        case 'Mrs. Dennis Schulist':
            split_name = name.split(' ')[1:]

        case 'Nicholas Runolfsdottir V':
            split_name = name.split(' ')[:2]

        case default:
            split_name = name.split(' ')
    
    return split_name

class Command(BaseCommand):

    def handle(self, *args, **options):

        User.objects.filter(is_superuser=False).delete()
        BlogPost.objects.all().delete()
        Comment.objects.all().delete()

        BASE_URL = "http://jsonplaceholder.typicode.com"

        for x in range(10):
            users = requests.get(BASE_URL + '/users').json()
            user_ids = []
            for user in users:
                username = user['username']
                email = user['email']
                name = user['name']

                first_name, last_name = split_name(name)

                new_user = User.objects.create_user(
                    username=username + str(x),
                    email=email,
                    password='pass3412',
                    first_name=first_name,
                    last_name=last_name
                )

                user_ids.append(new_user.id)

            # list of all the user ids
            blogpost_ids = []

            # create posts
            posts = requests.get(BASE_URL + '/posts').json()
            for post in posts:
                # user_id is the value at the index of the userId from the API
                user_id = user_ids[int(post['userId'])-1]
                user = User.objects.get(id=user_id)

                title = post['title']
                body = post['body']

                user = User.objects.get(id=user_id)

                new_blogpost = BlogPost.objects.create(
                    user=user,
                    title=title,
                    body=body
                )

                blogpost_ids.append(new_blogpost.id)


            # create comments
            comments = requests.get(BASE_URL + '/comments').json()
            for comment in comments:
                name = comment['name']
                body = comment['name']

                # user_id is the value at the index of the userId from the API
                blogpost_id = blogpost_ids[int(comment['postId'])-1]
                blogpost = BlogPost.objects.get(id=blogpost_id)

                new_comment = Comment.objects.create(
                    blogpost = blogpost,
                    name=name,
                    body=body
                )

