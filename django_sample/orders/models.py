from django.db import models

from projects.models import Project


class Order(models.Model):
    project = models.ForeignKey(Project)
