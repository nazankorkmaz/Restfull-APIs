# Generated by Django 5.0.6 on 2025-03-19 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=20),
        ),
    ]
