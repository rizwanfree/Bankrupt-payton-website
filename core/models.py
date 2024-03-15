from django.db import models
from django.urls import reverse
from  django.template.defaultfilters import slugify
from .utils import generate_slug

# Create your models here.


class Case(models.Model):
    case_no = models.CharField(max_length=100)
    district = models.CharField(max_length=50)
    chapter = models.IntegerField()
    assets = models.IntegerField()
    date_filed = models.CharField(null=True, blank=True, max_length=50)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255)
    ssn = models.CharField(max_length=50)
    street1 = models.CharField(max_length=255)
    street2 = models.CharField(max_length=255, null=True, blank=True)
    street3 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=10)
    zip = models.CharField(max_length=10)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ('first_name',)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.first_name + ' ' + self.last_name)
        return super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return f'/{self.slug}/
    




