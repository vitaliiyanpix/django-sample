from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'


class Technology(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    logo = models.ImageField(upload_to='services/technologies/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Technology'
        verbose_name_plural = 'Technologies'
