from django.conf import settings
from django.db import models
from django.utils import timezone

from phonenumber_field.modelfields import PhoneNumberField

TYPE_CHOICES = (
    ('tincture', 'Tincture'),
    ('dried', 'Dried'),
    ('oil', 'Oil'),
    ('glycerite', 'Glycerite'),
    ('tea_blend', 'Tea blend'),
    ('fire_cider', 'Fire cider'),
    ('salve', 'Salve'),
    ('throat_spray', 'Throat spray'),
    ('wound_spray', 'Wound spray'),
    ('bitters', 'Bitters'),
    ('syrup', 'Syrup'),
)

REMEDY_UNIT_CHOICES = (
    ('ounces', 'ounces'),
    ('1_oz_jar', '1 oz jars'),
    ('2_oz_jar', '2 oz jars'),
    ('4_oz_jar', '4 oz jars'),
)

class Herb(models.Model):
    common_name = models.CharField(max_length=100, blank=False)
    binomial = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return f'{self.common_name} ({self.binomial})'

class Donor(models.Model):
    name = models.CharField("donor's name", max_length=200, blank=False)
    phone = PhoneNumberField(blank=False)
    email = models.EmailField(blank=False)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.name

class SimpleInventory(models.Model):
    type = models.CharField(
        max_length = 20,
        choices = TYPE_CHOICES,
        default = 'tincture'
    )
    quantity = models.IntegerField(blank=False)
    herb = models.ForeignKey(
        Herb,
        on_delete=models.PROTECT
    )

    def __str__(self):
        return f'{self.herb} {self.type}'

class RemedyInventory(models.Model):
    name = models.CharField("remedy name", max_length=200, blank=False)
    herbs = models.ManyToManyField(Herb)
    quantity = models.IntegerField(blank=False)
    units = models.CharField(
        max_length = 20,
        choices = REMEDY_UNIT_CHOICES,
        default = 'ounces'
    )
    type = models.CharField(
        max_length = 20,
        choices = TYPE_CHOICES,
        default = 'tincture'
    )

    def __str__(self):
        return self.name

class Donation(models.Model):
    name = models.CharField("remedy name", max_length=200, blank=False)
    type = models.CharField(
        max_length = 20,
        choices = TYPE_CHOICES,
        default = 'tincture',
    )
    quantity = models.IntegerField(blank=False)
    units = models.CharField(
        max_length = 20,
        choices = REMEDY_UNIT_CHOICES,
        default = 'ounces'
    )
    source_of_herbs = models.TextField(blank=False)
    date_made = models.DateField(blank=False)
    best_by_date = models.DateField(blank=False)
    donor = models.ForeignKey(
        Donor,
        on_delete=models.PROTECT
    )
    herbs = models.ManyToManyField(Herb)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name
