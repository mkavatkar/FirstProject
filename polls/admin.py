from django.contrib import admin
from .models import Question, Choice


# Customise the admin form
class ChoiceAdmin(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text', 'pub_date', 'was_published_recently']
    search_fields = ['question_text']
    list_filter = ['pub_date']
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceAdmin]
# Register your models here.
admin.site.register(Question, QuestionAdmin)
