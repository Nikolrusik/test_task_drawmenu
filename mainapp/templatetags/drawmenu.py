from django import template
from mainapp.models import Menu

register = template.Library()

@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    menu = Menu.objects.filter(name=menu_name).first()
    if not menu:
        return ''

    request = context['request']
    current_url = request.path_info
    menu_html = '<ul>'
    for item in menu.children.all():
        menu_html += render_menu_item(item, current_url)
    menu_html += '</ul>'
    return menu_html

def render_menu_item(item, current_url):
    active_class = 'active' if item.url == current_url else ''
    menu_html = f'<li class="{active_class}"><a href="{item.url}">{item.name}</a>'
    if item.children.exists():
        menu_html += '<ul>'
        for child in item.children.all():
            menu_html += render_menu_item(child, current_url)
        menu_html += '</ul>'
    menu_html += '</li>'
    return menu_html
