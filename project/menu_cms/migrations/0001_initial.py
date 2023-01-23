# Generated by Django 4.0.4 on 2023-01-23 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Menu name')),
                ('display_name', models.CharField(max_length=100, verbose_name='Menu display')),
            ],
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('node_name', models.CharField(max_length=255, verbose_name='Node_name')),
                ('named_url', models.CharField(blank=True, max_length=255, null=True, verbose_name='named url default')),
                ('url', models.CharField(blank=True, max_length=255, null=True, verbose_name='URL')),
                ('menu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='menu_cms.menu')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='menu_cms.node')),
            ],
        ),
        migrations.AddField(
            model_name='menu',
            name='root_node',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='is_rood_node', to='menu_cms.node'),
        ),
    ]
