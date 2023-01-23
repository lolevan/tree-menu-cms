from django.db import models


class Menu(models.Model):
    name = models.CharField(verbose_name='Menu name')
    display_name = models.CharField()
    root_node = models.ForeignKey(to='Node', on_delete=models.CASCADE)


class Node(models.Model):
    node_name = models.CharField()
    named_url = models.URLField()
    url = models.URLField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)
