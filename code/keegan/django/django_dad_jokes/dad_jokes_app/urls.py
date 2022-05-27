from django.urls import path

# import views.py from the dad_jokes_app
from . import views

# namespace the app
app_name = 'dad_jokes_app'

# reference the path like this: "app_name:path_name"
urlpatterns = [
    # when the url localhost:8000/ is entered, load the index page
    path('', views.index, name="index"),
    path('jokes/', views.jokes_list, name="list")
]