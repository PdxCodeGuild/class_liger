from django.urls import  path
from . import views

app_name = 'study_app'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('', views.homepage, name='homepage'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('books/', views.books, name='books'),
    path('projects/', views.projects, name='projects'),
    path('profile/', views.profile, name='profile'),
    path('projects/<int:project_id>', views.projdetail, name='projdetail'),
    path('delete_proj/<int:project_id>', views.delete_proj, name='delete_proj'),
    
   
]