from django.contrib import admin
from .models import Question, Category,Level,Answer,user_progress

# Register your models here.
admin.site.register(Question)
admin.site.register(Category)
admin.site.register(Level)
admin.site.register(Answer)
admin.site.register(user_progress)
