from django.db import models
from django.urls import reverse
from  django.template.defaultfilters import slugify


# Create your models here.


ZONES = (
    ('EASTERN', 'EASTERN'),
    ('WESTERN', 'WESTERN'),
    ('SOUTHERN', 'SOUTHERN'),
    ('NORTHERN', 'NORTHERN'),
)


class State(models.Model):
    name = models.CharField(max_length=200)
    sn = models.CharField(max_length=3, blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        self.sn = self.sn.upper()
        super(State, self).save(*args, **kwargs)
    class Meta:
        ordering = ('name',)

class District(models.Model):
    state = models.ForeignKey(
        State, on_delete=models.CASCADE, blank=False, null=False)
    name = models.CharField(max_length=250, null=False, blank=False)
    zone = models.CharField(
        max_length=20, choices=ZONES, blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.zone})"

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        super(District, self).save(*args, **kwargs)


class Resource(models.Model):
    state = models.ForeignKey(
        State, on_delete=models.CASCADE, blank=False, null=False)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    city = models.CharField(max_length=250, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    tollFree = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        if self.city is None:
            return f"{self.district.name} ({self.district.zone})"
        else:
            return self.city.upper()

    def save(self, *args, **kwargs):
        if self.city is None:
            super(Resource, self).save(*args, **kwargs)
        else:
            self.city = self.city.upper()
            super(Resource, self).save(*args, **kwargs)


class Case(models.Model):
    name = models.CharField(max_length=250)
    caseNo = models.CharField(max_length=100)
    ch = models.IntegerField()    
    discharged = models.DateTimeField(null=True, blank=True)
    address = models.CharField(max_length=350)
    zip = models.CharField(max_length=25)
    state = models.ForeignKey(State, on_delete=models.PROTECT)
    filed = models.DateTimeField(null=True, blank=True)
    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("case-details", kwargs={"slug": self.slug})

    # def save(self, *args, **kwargs):
    #     #if not self.slug:
    #     self.slug = slugify(self.name + '-' + str(self.id))
    #     return super().save(*args, **kwargs)

# class State(models.Model):
#     name = models.CharField(max_length=200)
#     sn = models.CharField(max_length=3, blank=True, null=True)

#     def __str__(self):
#         return self.name
    
#     def save(self, *args, **kwargs):
#         self.name = self.name.upper()
#         self.sn = self.sn.upper()
#         super(State, self).save(*args, **kwargs)
    
#     class Meta:
#         ordering = ('name',)


# class Case(models.Model):
#     name = models.CharField(max_length=250)
#     caseNumber = models.CharField(max_length=50)
#     ch = models.IntegerField()    
#     discharged = models.DateField()
#     address = models.TextField()
#     zip = models.CharField(max_length=20, blank=True, null=True)
#     state_id = models.ForeignKey(State, on_delete=models.CASCADE)
#     bankruptcy = models.CharField(max_length=50)
#     filed = models.DateField()

#     def __str__(self):
#         return self.name