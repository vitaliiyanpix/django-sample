from django.contrib import admin

from . import models


class MemberInline(admin.TabularInline):
    model = models.Member
    extra = 1
    prepopulated_fields = {'slug': ('name',), }


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', )
    prepopulated_fields = {'slug': ('name',), }
    inlines = [MemberInline, ]


admin.site.register(models.Team, TeamAdmin)
