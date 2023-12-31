# Generated by Django 4.2.3 on 2023-07-27 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DemoApp', '0002_alter_order_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='price_individual',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
