from django.contrib import admin
from . import models


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'status', 'created_at', 'show')
    prepopulated_fields = {'slug': ('name', ), }
    list_editable = ('show', )


admin.site.register(models.Project, ProjectAdmin)
