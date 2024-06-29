# Generated by Django 5.0.4 on 2024-06-26 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AddField(
            model_name='fooditem',
            name='is_availabe',
            field=models.BooleanField(default=True),
        ),
    ]