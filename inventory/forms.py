from django import forms
from django.forms import ModelForm, DateInput
from inventory.models import Donation

class DonationForm(ModelForm):

    class Meta:
        model = Donation
        fields = '__all__'
        widgets = {
            'date_made': DateInput(attrs={'type': 'date'}),
            'best_by_date': DateInput(attrs={'type': 'date'})
        }

# class DispenseForm(Form):
    #TODO
