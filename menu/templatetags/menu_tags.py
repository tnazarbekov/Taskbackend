from django import template
from menu.models import MenuItem

register = template.Library()

@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    menu_items = MenuItem.objects.filter(menu_name=menu_name).select_related('parent').order_by('id')
    active_item = None
    for item in menu_items:
        if item.get_absolute_url() == request.path:
            active_item = item
            break
    return {
        'menu_items': menu_items,
        'active_item': active_item,
    }