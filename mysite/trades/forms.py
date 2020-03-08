from django import forms
from django.utils.translation import gettext_lazy as _

from .models import *

import datetime

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class AddTradeForm(forms.ModelForm):

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
        widgets = {
            'dateCreated': DateInput(),
            'maturityDate': DateInput(),
            'timeCreated': TimeInput(),
        }
        #localized_fields = ('dateCreated',)



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
            'dateCreated': DateInput(),
            'maturityDate': DateInput(),
            'timeCreated': TimeInput(),
        }
