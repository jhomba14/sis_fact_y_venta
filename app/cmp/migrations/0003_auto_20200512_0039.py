# Generated by Django 3.0.5 on 2020-05-12 05:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmp', '0002_comprasdet_comprasenc'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comprasenc',
            old_name='Proveedor',
            new_name='proveedor',
        ),
    ]
