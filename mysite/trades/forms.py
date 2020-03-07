from django import forms
from django.utils.translation import gettext_lazy as _

from .models import *

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
        help_texts = {
            'prodInfo': _('State the name/details of the product'),
        }
        # widgets = {
        #     'dateCreated': forms.DateInput(),
        # }
