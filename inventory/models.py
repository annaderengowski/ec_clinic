from django.conf import settings
from django.db import models
from django.utils import timezone

from phonenumber_field.modelfields import PhoneNumberField

class Herb(models.Model):
    common_name = models.CharField(max_length=100, blank=False)
    binomial = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return f'{self.common_name} ({self.binomial})'

class PreparationType(models.Model):
    name = models.CharField("name of preparation type", max_length=100, blank=False)

    def __str__(self):
        return self.name

class Volunteer(models.Model):
    name = models.CharField("name of volunteer", max_length=200, blank=False)
    phone = PhoneNumberField(blank=False)
    email = models.EmailField(blank=False)

    def __str__(self):
        return self.name

class Donor(models.Model):
    name = models.CharField("donor's name", max_length=200, blank=False)
    phone = PhoneNumberField(blank=False)
    email = models.EmailField(blank=False)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.name

# class Simple(model.Model): ???

class Remedy(models.Model):
    name = models.CharField("remedy name", max_length=200, blank=False)
    quantity = models.IntegerField(blank=False)
    units = models.CharField(max_length=30, blank=False)
    source_of_herbs = models.TextField(blank=False)
    date_made = models.DateField(blank=False)
    best_by_date = models.DateField(blank=False)
    contains_alcohol = models.BooleanField(default=False)
    donor = models.ForeignKey(
        Donor,
        on_delete=models.PROTECT
    )
    type = models.ForeignKey(
        PreparationType,
        on_delete=models.PROTECT
    )
    herbs = models.ManyToManyField(Herb)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name
