# Generated by Django 3.0.5 on 2020-05-27 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('new', 'New'), ('in_progress', 'In progress'), ('closed', 'Closed')], max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('order', models.PositiveIntegerField(unique=True)),
                ('logo', models.ImageField(upload_to='projects/')),
                ('technologies', models.ManyToManyField(blank=True, null=True, to='services.Technology')),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
                'ordering': ('order',),
            },
        ),
    ]