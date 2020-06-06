from django.contrib import admin

from .models import todoslist

class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(todoslist,TodoAdmin)
