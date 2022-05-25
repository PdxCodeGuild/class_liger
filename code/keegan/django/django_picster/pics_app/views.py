from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import JsonResponse # to return JSON in an HTTP response

from .models import Pic

from .forms import PicForm

def index(request):

    # get all the pics from the database
    pics = Pic.objects.all()

    context = {
        'pics': pics
    }

    return render(request, 'pics/index.html', context)


@login_required
def create(request):
    if request.method == 'GET':
        form = PicForm()
        
        context = {
            'form': form
        }

        return render(request, 'pics/create.html', context)

    elif request.POST:
        form = PicForm(request.POST)


        # get the picture file if it exists
        image = request.FILES.get('image')

        # form.initial is a dictionary with the original values
        # the form was instantiated with
        form.initial['image'] = image

        if form.is_valid():
            # commit = False will create the object, but won't save it
            new_pic = form.save(commit=False)

            # associate the logged in user with the pic
            new_pic.user = request.user

            # save the changes to the database
            new_pic.save()

        return redirect('pics_app:index')


@login_required
def update(request, pic_id):
    # get the currect Pic information from the db
    pic = get_object_or_404(Pic, id=pic_id)

    if request.method == 'GET':
        form = PicForm(instance=pic)

        context = {
            'form': form,
            'pic': pic
        }

        return render(request, 'pics/edit.html', context)

    if request.method == 'POST':
        # instantiate the PicForm with the data from the HTTP request and the pic instance
        form = PicForm(request.POST, instance=pic)

        # if a file was submitted in the form data,
        # add it to the PicForm's initial data
        image = request.FILES.get('image')
        if image:
            form.initial['image'] = image


        # if the form is valid, add
        if form.is_valid():
            form.save()

        # redirect to the pics detail view, passing the pic_id as a kwarg
        return redirect(reverse('pics_app:index'))#, kwargs={'pic_id': pic_id}))


@login_required
def like(request, pic_id):

    # get the pic from the database
    pic = get_object_or_404(Pic, id=pic_id)

    if request.user not in pic.likes.all():
        pic.likes.add(request.user)

    else:
        pic.likes.remove(request.user)

    # return JSON data with the pic id and a boolean indicating if the 
    # requesting user is in the list of likes for the pic
    return JsonResponse({
        # boolean indicating if the requesting user is in the list of likes
        'isLiked': request.user in pic.likes.all(),
        # number of users that have liked the pic
        'likeCount': pic.likes.count()
    })


    # if using django to submit the request:
    # return redirect('pics_app:index')


def delete(request, pic_id):
    pic = get_object_or_404(Pic, id=pic_id)

    pic.delete()

    return redirect('pics_app:index')