from django.contrib import admin
from projects.models import Projects
from interfaces.models import Interfaces
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    """定制化admin端"""
    #  列表字段展示控制
    list_display = ['name','leader','tester','status','create_date']
# 将mode注册到django的admin中
admin.site.register(Projects,ProjectAdmin)
admin.site.register(Interfaces)