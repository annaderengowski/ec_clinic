from django.forms import ModelForm
from inventory.models import Donation

class DonationForm(ModelForm):
    class Meta:
        model = Donation
        fields = '__all__'
