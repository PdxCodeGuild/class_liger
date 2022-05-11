from django.contrib import admin

# Register your models here.
from .models import TodoItem, Priority
admin.site.register([TodoItem, Priority])