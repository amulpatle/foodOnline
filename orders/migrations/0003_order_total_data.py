# Generated by Django 5.0.4 on 2024-07-29 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_vendors'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_data',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
