from django.contrib import admin

from .models import Question

admin.site.register(Question)  # Register the Question model in the admin panel

