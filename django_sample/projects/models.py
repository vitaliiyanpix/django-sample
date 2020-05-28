from django.db import models

from services.models import Technology


class Project(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('in_progress', 'In progress'),
        ('closed', 'Closed')
    ]

    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    order = models.PositiveIntegerField(unique=True)
    logo = models.ImageField(upload_to='projects/')
    show = models.BooleanField(default=False, verbose_name='Show in profile')
    technologies = models.ManyToManyField(Technology, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        ordering = ('order', )

