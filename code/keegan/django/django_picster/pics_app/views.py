from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required

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
def like(request, pic_id):
    # get the pic from the database
    pic = get_object_or_404(Pic, id=pic_id)

    if request.user not in pic.likes.all():
        pic.likes.add(request.user)

    else:
        pic.likes.remove(request.user)


    return redirect('pics_app:index')