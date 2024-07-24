from django.contrib import admin
from .models import MenuItem

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'menu_name', 'parent')

admin.site.register(MenuItem, MenuItemAdmin)