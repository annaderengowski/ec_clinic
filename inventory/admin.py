from django.contrib import admin
from .models import Herb, Donor, SimpleInventory, RemedyInventory, Donation

admin.site.register(Herb)
admin.site.register(Donor)
admin.site.register(SimpleInventory)
admin.site.register(RemedyInventory)
admin.site.register(Donation)
