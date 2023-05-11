from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Questions)
admin.site.register(Category)
admin.site.register(Levels)
admin.site.register(Answers)
