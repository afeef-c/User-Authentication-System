from django.contrib import admin
from .models import CustomUser,Log

admin.site.register(CustomUser)

admin.site.register(Log)

