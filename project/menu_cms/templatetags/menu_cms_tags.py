from django import template
from django.urls import reverse, resolve, Resolver404
from django.utils.html import mark_safe

from ..models import Menu, Node


register = template.Library()


def get_ancestors(node):
    pass


def draw_node(node):
    pass


def get_children(node):
    pass


@register.simple_tag(takes_context=True)
def draw_menu(context, name_menu):
    current_url = context.request.path
    html = ''

    try:
        current_url_name = resolve(current_url).url
    except Resolver404:
        current_url_name = None

    if current_url_name:
        active_node = Node.objects.filter(
            menu=Menu.objects.get(name=name_menu).id,
        ).get(named_url=current_url_name)
    elif current_url:
        active_node = Node.objects.filter(
            menu=Menu.objects.get(name=name_menu).id,
        ).get(named_url=current_url)

    active_node_parent = active_node.parent
    count_ul_blocks = 1
    if active_node_parent:
        ancestors = get_ancestors(active_node_parent)

        count_ul_blocks = len(ancestors) + 2
        for node in reversed(ancestors):
            html += f'<ul>{draw_node(node)}'

    html += f'<ul>{draw_node(active_node)}<ul>' # -> a
    children = get_children(active_node)

    for node in children:
        html += draw_node(node)
    html += '</ul>' * count_ul_blocks

    return mark_safe(html)
