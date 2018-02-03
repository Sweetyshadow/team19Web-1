from django.contrib import admin
from .models import TeamInfo, StudentInfo, RuleFile
# Register your models here.


class StudentAdmin(admin.TabularInline):
    model = StudentInfo
    extra = 3


class TeamAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['team_name']}),
        (None, {'fields': ['leader']}),
        (None, {'fields': ['invite_code']}),
        (None, {'fields': ['codes'], 'class': ['collapse']}),
        (None, {'fields': ['history'], 'class': ['collapse']}),
        (None, {'fields': ['score']}),
    ]

    list_display = ('team_name', 'leader', 'score')
    list_filter = ['team_name']


admin.site.register(TeamInfo)
admin.site.register(StudentInfo)
admin.site.register(RuleFile)
