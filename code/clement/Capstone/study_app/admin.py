from django.contrib import admin
from .models import Project, Resource

# Register your models here.
admin.site.register([Project, Resource])