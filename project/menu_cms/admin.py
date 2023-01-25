from django.contrib import admin

from .models import Menu, Node


class NodesInline(admin.StackedInline):
    model = Node
    extra = 2
    readonly_fields = [
        'menu',
        'parent',
    ]


class MenuAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'display_name', 'root_node']
    list_display_links = ['pk', 'name']
    readonly_fields = ['root_node']


class NodeAdmin(admin.ModelAdmin):
    list_display = ['pk', 'node_name', 'named_url', 'url', 'menu', 'parent']
    list_display_links = ['pk', 'node_name']
    list_editable = ['named_url', 'url']
    readonly_fields = ['menu', 'parent']
    inlines = [NodesInline]


admin.site.register(Menu, MenuAdmin)
admin.site.register(Node, NodeAdmin)
