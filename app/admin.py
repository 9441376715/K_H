from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(UserProfile)

admin.site.register(Topic)

admin.site.register(Blog_user)

admin.site.register(Blog_post)