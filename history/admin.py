from django.contrib import admin

from .models import History

class HistoryAdmin(admin.ModelAdmin):
    '''fieldsets = [
        ('Date information', {'fields': ['history_date']}),
        (None, {'fields': ['history_text']}),
    ]'''
    list_display = ('history_date', 'history_text')

admin.site.register(History, HistoryAdmin)