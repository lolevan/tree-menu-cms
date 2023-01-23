from django.db import models


class Menu(models.Model):
    """
    class describing the properties menu
    """
    name = models.CharField(
        verbose_name='Menu name',
        max_length=100,
        unique=True,
    )
    display_name = models.CharField(
        verbose_name='Menu display',
        max_length=100,
    )
    root_node = models.ForeignKey(
        to='Node',
        on_delete=models.CASCADE,
        related_name='is_rood_node',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name


class Node(models.Model):
    """
    class describing the properties node
    """
    node_name = models.CharField(
        verbose_name='Node_name',
        max_length=255,
    )
    named_url = models.CharField(
        verbose_name='named url default',
        max_length=255,
        null=True,
        blank=True,
    )
    url = models.CharField(
        verbose_name='URL',
        blank=True,
        null=True,
    )
    parent = models.ForeignKey(
        to='self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    menu = models.ForeignKey(
        to='Menu',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.node_name
