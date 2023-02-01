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

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if not self.root_node:
            root_node = Node()
            root_node.node_name = 'root'
            root_node.url = '/'
            root_node.named_url = self.name
            if not self.pk:
                super().save(force_insert, force_update, using, update_fields)
                force_insert = False
            root_node.menu = self
            root_node.save()
            self.root_node = root_node
        super().save(force_insert, force_update, using, update_fields)


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
        max_length=255,
        blank=True,
        null=True,
    )
    parent = models.ForeignKey(
        to='self',
        on_delete=models.CASCADE,
        related_name='child',
        null=True,
        blank=True,
    )
    menu = models.ForeignKey(
        to='Menu',
        on_delete=models.CASCADE,
        related_name='nodes',
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.node_name

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        try:
            parent_menu = self.parent.menu
            if parent_menu:
                self.menu = parent_menu
        except AttributeError:
            pass
        super().save(force_insert, force_update, using, update_fields)

    def clean(self):
        if not self.url and not self.named_url:
            raise ValueError(
                {'url': 'One of "URL" or "Named URL" should have a value.'}
            )
