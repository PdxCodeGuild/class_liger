from django.shortcuts import render

# Create your views here.



def create(request):

    return render(request, 'blog_app/create.html')

# ---------------------------------------------------------

def base(request):
    
    return render(request, 'blog_app/base.html')