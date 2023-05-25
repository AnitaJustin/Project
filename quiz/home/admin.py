from django.contrib import admin
from .models import Question, Category,Level,Answer

# Register your models here.
admin.site.register(Question)
admin.site.register(Category)
admin.site.register(Level)
admin.site.register(Answer)

