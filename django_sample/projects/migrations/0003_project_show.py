# Generated by Django 3.0.5 on 2020-05-27 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_project_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='show',
            field=models.BooleanField(default=False, verbose_name='Show in profile'),
        ),
    ]
