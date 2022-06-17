from .models import Project
from django.views import generic
from django.contrib import messages
from django.contrib.auth import (authenticate, login
as django_login, logout as django_logout)
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from . form import Project, Resource, ProjectForm, BookForm,RegisterForm


# =============================================================================================
# Create your views here.
def register(request):
    if request.method== "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"{username} account is successfully created...")
            return redirect('study_app:login')

    else:
        form = RegisterForm()

    context = {
        'form': form
    }

    return render(request, 'layout/register.html', context)

# ===============================================================================================

# Login View
def login(request):
    if request.method == "POST":
        form = request.POST

        username = form.get('username')
        password = form.get('password')

        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.error(request, f"{username} entered is not valid username or password")

            context ={
                
            }
            return render(request, 'layout/login.html', context)

        django_login(request, user)

        return redirect('study_app:homepage')


    elif request.method == "GET":
       

        context={
            
        }
        return render(request, 'layout/login.html', context)
# ===============================================================================================

@login_required
def homepage(request):
    return render(request, 'home/homepage.html')

@login_required
def projects(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = Project(user=request.user, title=request.POST['title'], description=request.POST['description'])
            project.save()

        messages.success(request, f"The project form {request.user.username} is successfully added....")
        return redirect('study_app:projects')

    elif request.method== "GET":
        form = ProjectForm()
    projects = Project.objects.filter(user=request.user)
    context={
        'projects': projects,
        'form':form 
    }
    return render(request, 'home/project.html', context)
# ===============================================================================================

@login_required
def profile(request):
    # homeworks = Homework.objects.filter(is_finalized=False, user=request.user)
    projects = Project.objects.filter(is_finished=False, user=request.user)

    # if len(homeworks)== 0:
    #     homework_done = True
    # else:
    #     homework_done = False

    if len(projects)== 0:
        project_done = True
    else:
        project_done = False

    context ={
        # 'homeworks':homeworks,
        'projects':projects,
        # 'homework_done':homework_done,
        'project_done':project_done,
    }

    return render(request, 'layout/profile.html', context)
# ===============================================================================================

def projdetail(request, project_id):

   
    project = get_object_or_404(Project, id=project_id)

    context = {
        'project': project
    }

    return render(request, 'home/projdetail.html', context)

# ===============================================================================================

def books(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = Resource(user=request.user, name=request.POST['name'], author=request.POST['author'], price=request.POST['price'], resources_type=request.POST['resources_type'], url=request.POST['url'])
            book.save()

        messages.success(request, f"The resource form {request.user.username} is successfully added....")
        return redirect('study_app:books')

    elif request.method== "GET":
        form = BookForm()
    books = Resource.objects.filter(author=request.author)

    context={
        'books': books,
        'form':form 
    }
    return render(request, 'home/book.html', context)
    

# =========================================================================================================

# fix the error when u come back form break
@login_required
def delete_proj(request, project_id):
    projects=Project.objects.get(id=project_id)
    projects.delete()
    return redirect('study_app:projects')


def logout(request):
    django_logout(request)
    return redirect( 'study_app:login')