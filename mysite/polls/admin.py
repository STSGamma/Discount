from django.contrib import admin

from .models import Question

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Evgeniy',              {'fields':['question_text']}),
        ('Date information', {'fields':['pub_date']}),
        ]
admin.site.register(Question, QuestionAdmin)

