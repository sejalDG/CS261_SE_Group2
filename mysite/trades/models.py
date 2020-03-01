import datetime

from django.db import models
from django.utils import timezone

class Trade(models.Model):
    dateCreated = models.DateField('date created')
    timeCreated = models.TimeField('time created')
    prodInfo = models.CharField(max_length=200)
    buyingPartyInfo = models.CharField(max_length=200)
    sellingPartyInfo = models.CharField(max_length=200)
    notionalAmount = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    maturityDate = models.DateField('maturity date')
    underlyingAmount = models.PositiveIntegerField()
    POUNDS = 'GBP'
    DOLLARS = 'USD'
    currencyChoices = [
        (POUNDS, 'Pounds'),
        (DOLLARS, 'Dollars'),
    ]
    underlyingCurrency = models.CharField(
        max_length=3,
        choices=currencyChoices,
        default=POUNDS,
    )
    strikePrice = models.DecimalField(max_digits=6, decimal_places=2)
    def __str__(self):
        return "Trade ID " + str(self.id)


# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     #pub_date = models.DateTimeField('date published')
#     # What to return when object is converted to a string
#     def __str__(self):
#         return self.question_text
