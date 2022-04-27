from django.contrib import admin

from .models import User

# register the User model in the admin panel
admin.site.register(User)