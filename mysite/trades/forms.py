from django import forms
from django.utils.translation import gettext_lazy as _

from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class AddTradeForm(forms.ModelForm):

    class Meta:
        model = Trade
        fields = '__all__'
        labels = {
            'dateCreated': _('Date Created (DD/MM/YYYY)'),
            'timeCreated': _('Time Created'),
            'prodInfo': _('Product Information'),
            'buyingPartyInfo': _('Buying Party Information'),
            'sellingPartyInfo': _('Selling Party Information'),
            'notionalAmount': _('Notional Amount'),
            'quantity': _('Quantity'),
            'maturityDate': _('Maturity Date (DD/MM/YYYY)'),
            'underlyingAmount': _('Underlying Amount'),
            'underlyingCurrency': _('Underlying Currency'),
            'strikePrice': _('Strike Price'),
        }
        widgets = {
            'timeCreated': TimeInput(),
        }

class EditTradeForm(forms.ModelForm):

    class Meta:
        model = Trade
        fields = '__all__'
        labels = {
            'dateCreated': _('Date Created'),
            'timeCreated': _('Time Created'),
            'prodInfo': _('Product Information'),
            'buyingPartyInfo': _('Buying Party Information'),
            'sellingPartyInfo': _('Selling Party Information'),
            'notionalAmount': _('Notional Amount'),
            'quantity': _('Quantity'),
            'maturityDate': _('Maturity Date'),
            'underlyingAmount': _('Underlying Amount'),
            'underlyingCurrency': _('Underlying Currency'),
            'strikePrice': _('Strike Price'),
        }
    #    help_texts = {
    #        'prodInfo': _('State the name/details of the product'),
    #    }
        widgets = {
            'timeCreated': TimeInput(),
        }
