from django.contrib import admin

from .models import Question, Choice

admin.site.site_header = 'Polls Project'


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 1


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'open', )
    list_filter = ('open', )
    inlines = [ChoiceInline]
