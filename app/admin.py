from django.contrib import admin
from .models import Category, QuestionPaper, Questions
# Register your models here.

admin.site.register(Category)

admin.site.register(QuestionPaper)


admin.site.register(Questions)
