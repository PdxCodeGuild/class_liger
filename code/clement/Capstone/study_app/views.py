from .models import Project
from django.contrib import messages
from django.contrib.auth import (authenticate, login
as django_login, logout as django_logout)
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from . form import Project, Resource, ProjectForm, ResourceForm,RegisterForm,DictionaryForm


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


# ===========================================================================================

def flashcards(request):
    return render(request, 'layout/flashcards.html')


# ===============================================================================================

# Login View
def login(request):
    if request.method == "POST":
        form = request.POST

        username = form.get('username')
        password = form.get('password')

        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.error(request, "Invalid username or password")

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

# =============================================================================================== 

@login_required
def projects(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = Project(user=request.user, title=request.POST['title'], description=request.POST['description'])
            project.save()

        messages.success(request, f"The project created by {request.user.username} is successfully added....")
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
    projects = Project.objects.filter(is_finished=False, user=request.user)
    resources = Resource.objects.filter(name=request.user)

    # homeworks = Homework.objects.filter(is_finalized=False, user=request.user)
    # if len(homeworks)== 0:
    #     homework_done = True
    # else:
    #     homework_done = False

    if len(projects)== 0:
        project_done = True
    else:
        project_done = False

    context ={
        'projects':projects,
        'project_done':project_done,
        'resources': resources,
        # 'homeworks':homeworks,
        # 'homework_done':homework_done,
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
@login_required
def resource(request):
    if request.method == "POST":
        form = ResourceForm(request.POST)
        if form.is_valid():
            resource = Resource(name=request.POST['name'], author=request.POST['author'], price=request.POST['price'], resources_type=request.POST['resources_type'], url=request.POST['url'])
            resource.save()

        messages.success(request, f"The resource added by {request.user.username} is successful....")
        return redirect('study_app:resource')

    elif request.method== "GET":
        form = ResourceForm()
        resources = Resource.objects.filter(name=request.user)
        projects = Project.objects.filter(user=request.user)
    
        context={
            'resources': resources,
            'form':form, 
            'projects':projects
        } 
    return render(request, 'home/resource.html', context)
    

# ===============================================================================================

def resourcedetail(request, resource_id):
    resources = get_object_or_404(Resource, id=resource_id)
    context = {
        'resources': resources
    }
    return render(request, 'home/resourcedetail .html', context)
# ===================================================================================================

# fix the error when u come back form break
@login_required
def delete_proj(request, project_id):
    projects=get_object_or_404(Project, id=project_id)
    projects.delete()
    return redirect('study_app:projects')

@login_required
def deleteresource(request, resource_id):
    resources=Resource.objects.get(Resource, id=resource_id)
    resources.delete()
    return redirect('study_app:resource')

def logout(request):
    django_logout(request)
    return redirect( 'study_app:login')
# ==========================================================================================

def addresources(request, project_id):
    if request.method == "POST":
        project = Project.objects.get(id=project_id)
        form = ResourceForm(request.POST or None)
        if form.is_valid():

            new_resource = form.save()
            new_resource.projects.add(project)
           
            messages.success(request, "The resource is added successfully.....")

        return redirect('study_app:projdetail', project_id)

    else:
        project =Project.objects.get(id=project_id)
        form = ResourceForm()
        context = {
            'project': project,
            'form': form
        }
    return render(request, 'home/addresources.html', context)

# ============================================================================================

def flashcards(request):
    return render(request, 'layout/flashcards.html')

def dictionary(request):
    form = DictionaryForm()
    context= {
        'form': form
    }
    return render(request, 'home/dictionary.html', context)