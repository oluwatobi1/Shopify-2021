# Generated by Django 3.1.5 on 2021-01-09 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_shop_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shop',
            name='price',
        ),
    ]
