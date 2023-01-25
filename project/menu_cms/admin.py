from django.contrib import admin

from .models import Menu, Node


class MenuAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'display_name', 'root_node']
    list_display_links = ['pk', 'name']
    readonly_fields = ['root_node']


class NodeAdmin(admin.ModelAdmin):
    list_display = ['pk', 'node_name', 'named_url', 'url', 'menu', 'parent']
    list_display_links = ['pk', 'node_name']
    readonly_fields = ['menu', 'parent']


admin.site.register(Menu, MenuAdmin)
admin.site.register(Node, NodeAdmin)
