from django.db import models

from services.models import Technology


def team_directory_path(instance, filename):
    return f'teams/{instance.name}/{filename}'


class Team(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    logo = models.ImageField(upload_to=team_directory_path)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'


def member_directory_path(instance, filename):
    return f'teams/{instance.team}/members/{filename}'


class Member(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    position = models.CharField(max_length=150)
    about = models.TextField()
    photo = models.ImageField(upload_to=member_directory_path)
    skills = models.ManyToManyField(Technology)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Member'
        verbose_name_plural = 'Members'

