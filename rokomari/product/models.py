from django.db import models
from django.urls import reverse

class Writer(models.Model):
    name = models.CharField(max_length=150)
    photo = models.ImageField(blank=True, null=True,upload_to='writer')
    description = models.TextField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('writer-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class Publication(models.Model):
    name = models.CharField(max_length=250)
    photo = models.ImageField(blank=True,null=True,upload_to='publication')

    def get_absolute_url(self):
        return reverse('publication-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name



class Subject(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name
