# Generated by Django 3.2.9 on 2021-11-29 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20211127_2203'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sold',
            field=models.TextField(blank=True),
        ),
    ]
