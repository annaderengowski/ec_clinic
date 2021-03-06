from django.contrib import admin
from .models import Herb, PreparationType, Volunteer, Donor, Remedy

admin.site.register(Herb)
admin.site.register(PreparationType)
admin.site.register(Volunteer)
admin.site.register(Donor)
admin.site.register(Remedy)
