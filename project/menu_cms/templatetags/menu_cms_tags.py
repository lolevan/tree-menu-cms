from django import template
from project.menu_cms.models import Menu, Node


register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    pass

