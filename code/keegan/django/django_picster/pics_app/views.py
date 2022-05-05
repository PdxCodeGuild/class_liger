from django.shortcuts import render

from .models import Pic

def index(request):

    # get all the pics from the database
    pics = Pic.objects.all()

    context = {
        'pics': pics
    }

    return render(request, 'pics/index.html', context)