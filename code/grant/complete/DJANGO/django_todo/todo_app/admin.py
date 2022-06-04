from django.contrib import admin

# Register your models here.
from .models import Priority, Todo

admin.site.register([Priority, Todo])
