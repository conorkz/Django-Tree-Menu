from django.contrib import admin
from my_app.models import MenuItem

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'menu_name', 'url')

admin.site.register(MenuItem, MenuItemAdmin)
