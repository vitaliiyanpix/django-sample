# Generated by Django 3.0.5 on 2020-05-28 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample_auth', '0002_auto_20200526_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='sampleuser',
            name='role',
            field=models.CharField(choices=[('staff', 'staff'), ('provider', 'provider'), ('customer', 'customer')], default='customer', max_length=20),
        ),
    ]