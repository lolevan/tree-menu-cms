from django.contrib import admin
from django.urls import reverse
from django.utils.html import mark_safe

from .models import Menu, Node


class NodesInline(admin.StackedInline):
    """class for embedding nodes"""
    model = Node
    extra = 2
    readonly_fields = [
        'node_edit',
        'menu',
        'parent',
    ]

    @staticmethod
    def node_edit(node):
        """function for edit node"""
        if node.pk:
            name_app = node._meta.app_label
            name_model = node._meta.model_name
            edit_url = reverse(
                viewname=f'admin:{name_app}_{name_model}_change',
                args=[node.pk]
            )

            return mark_safe(f'<a href="{edit_url}">Edit node</a>')

        return ''


class MenuAdmin(admin.ModelAdmin):
    """class for setting models admin"""
    list_display = ['pk', 'name', 'display_name', 'root_node']
    list_display_links = ['pk', 'name']
    readonly_fields = ['root_node']


class NodeAdmin(admin.ModelAdmin):
    """class for setting nodes admin"""
    list_display = ['pk', 'node_name', 'named_url', 'url', 'menu', 'parent']
    list_display_links = ['pk', 'node_name']
    list_editable = ['named_url', 'url']
    readonly_fields = ['menu', 'parent']
    inlines = [NodesInline]


admin.site.register(Menu, MenuAdmin)
admin.site.register(Node, NodeAdmin)
