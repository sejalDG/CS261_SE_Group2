from django import forms

from .models import *

class AddTradeForm(forms.ModelForm):

    class Meta:
        model = Trade
        fields = '__all__'

# def trade_new(request):
#     form = AddTradeForm()
#     return render(request, 'trades/addtradepage.html', {'form': form})
