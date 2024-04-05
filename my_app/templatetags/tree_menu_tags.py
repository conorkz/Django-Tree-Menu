from django import template
from django.urls import resolve
from my_app.models import MenuItem

register = template.Library()

@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    current_url = resolve(request.path_info).url_name  
    menu_items = MenuItem.objects.filter(menu_name=menu_name).order_by('parent') 

    def build_menu(items, parent_active):
        html = "<ul>"
        for item in items:
            is_active = item.get_absolute_url() == request.path or item.url_name == current_url
            has_children = items.filter(parent=item).exists()
            html += "<li>"
            html += f"<a href='{item.get_absolute_url()}'>{item.name}</a>"
            if (parent_active or is_active) and has_children:
                html += build_menu(items.filter(parent=item), is_active)
            html += "</li>"
        html += "</ul>"
        return html

    return build_menu(menu_items.filter(parent=None), False) 
