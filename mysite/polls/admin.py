from django.contrib import admin
from polls.models import Poll, Choice

# Register your models here.


class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3


class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question']}),
        ("Date Published", {'fields': ['pub_date']})
    ]

    list_display = ('question', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question']

    inlines = [ChoiceInLine]

admin.site.register(Poll, PollAdmin)
