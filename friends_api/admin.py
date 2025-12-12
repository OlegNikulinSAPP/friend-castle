from django.contrib import admin
from .models import Hobby, Friend, Meeting

# Регистрируем все три модели
admin.site.register(Hobby)
admin.site.register(Friend)
admin.site.register(Meeting)
