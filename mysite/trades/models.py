#import datetime
from datetime import date, datetime
from django.db import models
from django.utils import timezone

# dateToday = date.today().strftime("%d/%m/%Y")
# timeNow = datetime.now().strftime("%H:%M:%S")

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
    strikePrice = models.FloatField()
    def __str__(self):
        return "Trade ID " + str(self.id)

class strikePrice(models.Model):
    product = models.CharField(max_length=200)
    buyer = models.CharField(max_length=200)
    seller = models.CharField(max_length=200)
    mean = models.FloatField()
    standard_deviation = models.FloatField()
    min = models.FloatField()
    max = models.FloatField()
    count = models.PositiveIntegerField()

class underlyingPrice(models.Model):
    product = models.CharField(max_length=200)
    buyer = models.CharField(max_length=200)
    seller = models.CharField(max_length=200)
    mean = models.FloatField()
    standard_deviation = models.FloatField()
    min = models.FloatField()
    max = models.FloatField()
    count = models.PositiveIntegerField()

class quantityEstimate(models.Model):
    product = models.CharField(max_length=200)
    buyer = models.CharField(max_length=200)
    seller = models.CharField(max_length=200)
    mean = models.FloatField()
    standard_deviation = models.FloatField()
    min = models.FloatField()
    max = models.FloatField()
    count = models.PositiveIntegerField()

class notionalAmount(models.Model):
    product = models.CharField(max_length=200)
    buyer = models.CharField(max_length=200)
    seller = models.CharField(max_length=200)
    mean = models.FloatField()
    standard_deviation = models.FloatField()
    min = models.FloatField()
    max = models.FloatField()
    count = models.PositiveIntegerField()

class currencyValue(models.Model):
    date = models.DateField('date created')
    POUNDS = 'GBP'
    DOLLARS = 'USD'
    currencyChoices = [
        (POUNDS, 'Pounds'),
        (DOLLARS, 'Dollars'),
    ]
    currency = models.CharField(
        max_length=3,
        choices=currencyChoices,
        default=POUNDS,
    )
    valueInUSD = models.FloatField()

class stockPrice(models.Model):
    date = models.DateField('date created')
    companyID = models.CharField(max_length=200)
    stockPrice = models.FloatField()


# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     #pub_date = models.DateTimeField('date published')
#     # What to return when object is converted to a string
#     def __str__(self):
#         return self.question_text
