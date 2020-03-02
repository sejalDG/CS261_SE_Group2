import pandas as pd
import statistics
from array import *

# input a csv file here
# database simulated
df = pd.read_csv("09022015.csv")
tradeID = df.tradeID
product = df.product
buyingParty = df.buyingParty
sellingParty = df.sellingParty
notionalAmount = df.notionalAmount
notionalCurrency = df.notionalCurrency
quantity = df.quantity
maturityDate = df.maturityDate
underlyingPrice = df.underlyingPrice
underlyingCurrency = df.underlyingCurrency
strikePrice = df.strikePrice

buying_party_list = []
selling_party_list = []

tuple = ("09/02/2015 09:54", "HSUOFMWX18279783", "3D Maneuver Gears",
         "XRBV61", "NXTO39", 43440.32, "LKR", 10000, 16 / 11 / 2018,
         3.01, "USD", 5.03)


# ID check for uniqueness in input
# returns 0 if an ID already found
def trade_id_check(newID):
    for row in tradeID:
        if row.casefold() == newID.casefold():
            return 0
    return 1


# check if known product is being sent
# locates dictionary related to product being sent
def product_check(new_product):
    for row in product:
        if row.casefold() == new_product.casefold():
            return 0
    return 1


# checks if current input is a new buying party
# if new buying party no historical data available therefore all further suggestions ignored
def buying_party_check():
    for row in buyingParty:
        if row not in buying_party_list:
            buying_party_list.append(row)


def selling_party_check():
    for row in sellingParty:
        if row not in selling_party_list:
            selling_party_list.append(row)


# function that returns 0 if notional amount input is within suggested amount
# returns the estimate value if input is not within bounds
def notional_amount_check(current_notional):
    current_product = tuple.index(2)
    current_buyer = tuple.index(3)
    current_seller = tuple.index(4)

    estimate = get_notional_estimate(current_product, current_buyer, current_seller)
    standard_deviation = get_notional_standard_deviation(current_product, current_buyer, current_seller)
    standard_deviation_multiplier = 5
    standard_deviation_check = standard_deviation_multiplier * standard_deviation
    lower_bound = estimate - standard_deviation_check
    higher_bound = estimate + standard_deviation_check

    if lower_bound < current_notional < higher_bound:
        return 0
    else:
        return estimate


# finds the mean value of all the valid notional value inputs
# inputs: current input of product, buyer and seller identifiers
# checks database of estimates and returns its value
def get_notional_estimate(c_product, c_buyer, c_seller):
    return 0


# gets value of standard deviation of notional amount taken from all transactions of the same product between same
# buyer and seller inputs include the current product, buyer and seller that user inputs
def get_notional_standard_deviation(c_product, c_buyer, c_seller):
    return 0


# assuming previous data is already entered

# def notional_currency_check():

# function that returns 0 if quantity input is within suggested amount
# returns the estimate value if input is not within bounds
def quantity_check(current_quantity):
    current_product = tuple.index(2)
    current_buyer = tuple.index(3)
    current_seller = tuple.index(4)

    estimate = get_quantity_estimate(current_product, current_buyer, current_seller)
    standard_deviation = get_quantity_standard_deviation(current_product, current_buyer, current_seller)
    standard_deviation_multiplier = 5
    standard_deviation_check = standard_deviation_multiplier * standard_deviation
    lower_bound = estimate - standard_deviation_check
    higher_bound = estimate + standard_deviation_check

    if lower_bound < current_quantity < higher_bound:
        return 0
    else:
        return estimate


# finds the mean value of all the quantity
# inputs: current input of product, buyer and seller identifiers
# checks database of estimates and returns its value
def get_quantity_estimate(c_product, c_buyer, c_seller):
    return 0


# gets value of standard deviation of quantity taken from all transactions of the same product between same buyer and
# seller. inputs include the current product, buyer and seller that user inputs
def get_quantity_standard_deviation(c_product, c_buyer, c_seller):
    return 0


#
# def maturity_date_check():
#


# finds the mean value of all the underlying price
# inputs: current input of product, buyer and seller identifiers
# checks database of estimates and returns its value
def get_underlying_price_estimate(current_product, current_buyer, current_seller):
    return 0
    pass


# gets value of standard deviation of underlying price taken from all transactions of the same product between same
# buyer and seller. inputs include the current product, buyer and seller that user inputs
def underlying_price_standard_deviation(current_product, current_buyer, current_seller):
    return 0
    pass


# function that returns 0 if underlying price input is within suggested amount
# returns the estimate value if input is not within bounds
def underlying_price_check(current_underlying_price):
    current_product = tuple.index(2)
    current_buyer = tuple.index(3)
    current_seller = tuple.index(4)

    estimate = get_underlying_price_estimate(current_product, current_buyer, current_seller)
    standard_deviation = underlying_price_standard_deviation(current_product, current_buyer, current_seller)
    standard_deviation_multiplier = 5
    standard_deviation_check = standard_deviation_multiplier * standard_deviation
    lower_bound = estimate - standard_deviation_check
    higher_bound = estimate + standard_deviation_check

    if lower_bound < current_underlying_price < higher_bound:
        return 0
    else:
        return estimate


# def underlying_currency_check():
#
# finds the mean value of all the strike price
# inputs: current input of product, buyer and seller identifiers
# checks database of estimates and returns its value
def get_strike_price_estimate(current_product, current_buyer, current_seller):
    return 0
    pass


# gets value of standard deviation of strike price
# taken from all transactions of the same product between same
# buyer and seller. inputs include the current product, buyer and seller that user inputs
def strike_price_standard_deviation(current_product, current_buyer, current_seller):
    return 0
    pass


# function that returns 0 if strike price input is within suggested amount
# returns the estimate value if input is not within bounds
def strike_price_check(current_strike_price):
    current_product = tuple.index(2)
    current_buyer = tuple.index(3)
    current_seller = tuple.index(4)

    estimate = get_strike_price_estimate(current_product, current_buyer, current_seller)
    standard_deviation = strike_price_standard_deviation(current_product, current_buyer, current_seller)
    standard_deviation_multiplier = 5
    standard_deviation_check = standard_deviation_multiplier * standard_deviation
    lower_bound = estimate - standard_deviation_check
    higher_bound = estimate + standard_deviation_check

    if lower_bound < current_strike_price < higher_bound:
        return 0
    else:
        return estimate
