# Generated by Django 4.2.3 on 2023-07-27 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DemoApp', '0004_alter_order_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
    ]