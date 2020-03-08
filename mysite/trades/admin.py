from django.contrib import admin

from .models import Trade, strikePrice, underlyingPrice, quantityEstimate, notionalAmount, currencyValue, stockPrice, Report

admin.site.register(Trade)
admin.site.register(strikePrice)
admin.site.register(underlyingPrice)
admin.site.register(quantityEstimate)
admin.site.register(notionalAmount)
admin.site.register(currencyValue)
admin.site.register(stockPrice)
admin.site.register(Report)
