from django.contrib import admin

from .models import Poll

admin.site.site_header = 'Polls Project'


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = ('text', 'open', )
    list_filter = ('open', )
