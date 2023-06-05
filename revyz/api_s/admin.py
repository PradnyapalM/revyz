from django.contrib import admin
from .models import api_s

class api_sAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Address', 'City', 'Number', 'Email', 'Tech_skill']

# Register your models here.
admin.site.register(api_s, api_sAdmin)