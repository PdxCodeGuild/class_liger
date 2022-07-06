from django.urls import  path
from . import views




app_name = 'study_app'

urlpatterns = [

    #================ Users Views ================#

    path('login/', views.login, name='login'),
    path('', views.homepage, name='homepage'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),


    #================ Projects Views ================#

    path('projects/', views.projects, name='projects'),
    path('projects/<int:project_id>', views.projdetail, name='projdetail'),
    path('delete_proj/<int:project_id>', views.delete_proj, name='delete_proj'),


     #================ Resources Views ================#

    path('resource/', views.resource, name='resource'),
    path('resources/<int:resource_id>', views.resourcedetail, name='resourcedetail'),
    path('deleteresource/<int:resource_id>', views.deleteresource, name='deleteresource'),
    path('addresources/<int:project_id>', views.addresources, name='addresources'),

    
    #================ FlashCards Views ================#

    path('flashcards/', views.flashcards, name='flashcards'),
    path('dictionary/', views.dictionary, name='dictionary')

]