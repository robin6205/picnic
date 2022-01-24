from django.contrib import admin

# Register your models here.
from .models import Question, Restaurant

admin.site.register(Question)
admin.site.register(Restaurant)