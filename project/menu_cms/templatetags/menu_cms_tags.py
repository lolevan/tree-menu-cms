from django import template
from django.urls import reverse, resolve, Resolver404
from django.utils.html import mark_safe

from ..models import Menu, Node


register = template.Library()


def get_ancestors(node):
    """function for getting ancestors"""
    ancestors = []
    while node:
        ancestors.append(node)
        node = node.parent

    return ancestors


def draw_node(node, active=False):
    """function for substituting links and name"""
    if node.named_url:
        url = reverse(node.named_url)
    else:
        url = node.url
    if active:
        html = f'<li><a href={url}><b>{node.node_name}</b></a></li>'
    else:
        html = f'<li><a href={url}>{node.node_name}</a></li>'
    return html


def get_children(node):
    """function for giving back child objects"""
    children = []
    for child in node.child.all():
        children.append(child)

    return children


@register.simple_tag(takes_context=True)
def draw_menu(context, name_menu):
    """function for menu output"""
    current_url = context.request.path
    html = ''
    # get url_name
    try:
        current_url_name = resolve(current_url).url_name
    except Resolver404:
        current_url_name = None
    # get active_node
    if current_url_name:
        active_node = Node.objects.filter(
            menu=Menu.objects.get(name=name_menu).pk
        ).get(named_url=current_url_name)
    elif current_url:
        active_node = Node.objects.filter(
            menu=Menu.objects.get(name=name_menu).pk
        ).get(url=current_url)
    # get active node parents
    active_node_parent = active_node.parent
    count_ul_blocks = 1
    if active_node_parent:
        ancestors = get_ancestors(active_node_parent)

        count_ul_blocks = len(ancestors) + 2
        for node in reversed(ancestors):
            html += f'<ul>{draw_node(node)}'
    # draw active node
    html += f'<ul>{draw_node(active_node, active=True)}<ul>'
    children = get_children(active_node)
    # draw children
    for node in children:
        html += draw_node(node)
    html += '</ul>' * count_ul_blocks

    return mark_safe(html)
