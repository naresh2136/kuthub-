from django.contrib import admin
from mug.models import *
# Register your models here.
class SearchAdmin(admin.ModelAdmin):
    list_display = ['name','age','mail']

admin.site.register(Search,SearchAdmin)
