from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=64, unique=True)
    overview = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='project_images', blank=True, null=True)
    technologies = models.TextField(blank=True, null=True)
    functions = models.TextField(blank=True, null=True)
    link = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
