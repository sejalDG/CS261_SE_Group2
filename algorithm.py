import pandas as pd
import math
from array import *

# input a csv file here
# database simulated
df = pd.read_csv("03022015.csv")
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

tuple_data = ("09/02/2015 09:54", "HSUOFMWX18279783", "3D Maneuver Gears",
              "XRBV61", "NXTO39", 43440.32, "LKR", 10000, 16 / 11 / 2018,
              3.01, "USD", 5.03)


# checks if current input of product, buyer and seller has already been processed
# returns 1 if already in database
# returns 0 if not in database
def index_check(c_product, c_buyer, c_seller):
    is_indexed = 0
    if is_indexed == 1:
        return 1
    else:
        return 0


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
# Returns 0 if no estimate available
# returns the estimate value if input is not within bounds
def notional_amount_check(current_notional):
    current_product = tuple_data.index(2)
    current_buyer = tuple_data.index(3)
    current_seller = tuple_data.index(4)

    if index_check == 0:
        new_notional_estimate()
        return 0
    else:
        estimate = get_notional_estimate(current_product, current_buyer, current_seller)
        mean = estimate[3]
        standard_deviation = estimate[4]
        standard_deviation_multiplier = 5
        standard_deviation_check = standard_deviation_multiplier * standard_deviation
        lower_bound = mean - standard_deviation_check
        higher_bound = mean + standard_deviation_check

        if lower_bound < current_notional < higher_bound:
            update_notional_amount(estimate, current_notional)
            return 0
        else:
            return estimate


# updates rows in database with new notional estimate
# current row and new notional amount are inputs
def update_notional_amount(database_row, current_notional):
    # [0] = product name ; [1] = buyer; [2] = seller; [3] mean, [4] standard deviation;
    # [5] = min value; [6] = max value; [7] = count
    count = database_row[7]
    count = count + 1
    old_mean = database_row[3]
    new_mean = ((database_row[3] / count) + current_notional) / count

    old_standard_deviation = database_row[4]
    new_standard_deviation = math.sqrt((((count - 2) * (old_standard_deviation ** 2)) + ((count - 1) *
    ((old_mean - new_mean) ** 2)) + ((current_notional - new_mean) ** 2)) / (count - 1))

    # update min/max values if necessary
    if current_notional < database_row[5]:
        database_row[5] = current_notional
    elif current_notional > database_row[6]:
        database_row[6] = current_notional

    database_row[3] = new_mean
    database_row[4] = new_standard_deviation
    database_row[7] = count

    # update row in table

    pass


# function that creates new entry for current product, buyer and seller
# sets the values to their default
def new_notional_estimate(c_product, c_buyer, c_seller, current_notional):
    # update table
    max = current_notional
    min = current_notional
    mean = current_notional
    stdev = 0


# finds the mean value of all the valid notional value inputs
# inputs: current input of product, buyer and seller identifiers
# checks database of estimates and returns its value
# gets value of standard deviation of notional amount taken from all transactions of the same product between same
def get_notional_estimate(c_product, c_buyer, c_seller):
    # [0] = product name ; [1] = buyer; [2] = seller; [3] mean, [4] standard deviation;
    # [5] = min value; [6] = max value; [7] = count
    database_row = ("3D Maneuver Gears", "XRBV61", "NXTO39", 3500, 250, 300, 4700, 20)

    return database_row


# assuming previous data is already entered

# def notional_currency_check():


# function that returns 0 if quantity input is within suggested amount
# returns the estimate value if input is not within bounds
def quantity_check(current_quantity):
    current_product = tuple_data.index(2)
    current_buyer = tuple_data.index(3)
    current_seller = tuple_data.index(4)

    if index_check == 0:
        new_notional_estimate()
        return 0
    else:
        estimate = get_notional_estimate(current_product, current_buyer, current_seller)
        mean = estimate[3]
        standard_deviation = estimate[4]
        standard_deviation_multiplier = 5
        standard_deviation_check = standard_deviation_multiplier * standard_deviation
        lower_bound = mean - standard_deviation_check
        higher_bound = mean + standard_deviation_check

        if lower_bound < current_quantity < higher_bound:
            update_notional_amount(estimate, current_quantity)
            return 0
        else:
            return estimate


# updates rows in database with new quantity estimate
# current row and new notional amount are inputs
def update_quantity(database_row, current_quantity):
    # [0] = product name ; [1] = buyer; [2] = seller; [3] mean, [4] standard deviation;
    # [5] = min value; [6] = max value; [7] = count
    count = database_row[7]
    count = count + 1
    old_mean = database_row[3]
    new_mean = ((database_row[3] / count) + current_quantity) / count

    old_standard_deviation = database_row[4]
    new_standard_deviation = math.sqrt((((count - 2) * (old_standard_deviation ** 2)) + ((count - 1) * ((old_mean - new_mean) ** 2)) + (
            (current_quantity - new_mean) ** 2)) / (count - 1))

    # update min/max values if necessary
    if current_quantity < database_row[5]:
        database_row[5] = current_quantity
    elif current_quantity > database_row[6]:
        database_row[6] = current_quantity

    database_row[3] = new_mean
    database_row[4] = new_standard_deviation
    database_row[7] = count

    # update row in table

    pass


# finds the mean value of all the valid quantity value inputs
# inputs: current input of product, buyer and seller identifiers
# checks database of estimates and returns its value
# gets value of standard deviation of notional amount taken from all transactions of the same product between same
def get_quantity_estimate(c_product, c_buyer, c_seller):
    # [0] = product name ; [1] = buyer; [2] = seller; [3] mean, [4] standard deviation;
    # [5] = min value; [6] = max value; [7] = count
    database_row = ("3D Maneuver Gears", "XRBV61", "NXTO39", 3500, 250, 300, 4700, 20)

    return database_row


# function that creates new entry for current product, buyer and seller
# sets the values to their default
def new_quantity_estimate(c_product, c_buyer, c_seller, current_quantity):
    # update table
    max = current_quantity
    min = current_quantity
    mean = current_quantity
    stdev = 0


# function that returns 0 if underlying price input is within suggested amount
# returns the estimate value if input is not within bounds
def underlying_price_check(current_underlying_price):
    current_product = tuple_data.index(2)
    current_buyer = tuple_data.index(3)
    current_seller = tuple_data.index(4)

    if index_check == 0:
        new_notional_estimate()
        return 0
    else:
        estimate = get_notional_estimate(current_product, current_buyer, current_seller)
        mean = estimate[3]
        standard_deviation = estimate[4]
        standard_deviation_multiplier = 5
        standard_deviation_check = standard_deviation_multiplier * standard_deviation
        lower_bound = mean - standard_deviation_check
        higher_bound = mean + standard_deviation_check

        if lower_bound < current_underlying_price < higher_bound:
            update_notional_amount(estimate, current_underlying_price)
            return 0
        else:
            return estimate


# updates rows in database with new underlying_price estimate
# current row and new notional amount are inputs
def update_underlying_price(database_row, current_underlying_price):
    # [0] = product name ; [1] = buyer; [2] = seller; [3] mean, [4] standard deviation;
    # [5] = min value; [6] = max value; [7] = count
    count = database_row[7]
    count = count + 1
    old_mean = database_row[3]
    new_mean = ((database_row[3] / count) + current_underlying_price) / count

    old_standard_deviation = database_row[4]
    new_standard_deviation = math.sqrt((((count - 2) * (old_standard_deviation ** 2)) + ((count - 1) * ((old_mean - new_mean) ** 2)) + (
            (current_underlying_price - new_mean) ** 2)) / (count - 1))

    # update min/max values if necessary
    if current_underlying_price < database_row[5]:
        database_row[5] = current_underlying_price
    elif current_underlying_price > database_row[6]:
        database_row[6] = current_underlying_price

    database_row[3] = new_mean
    database_row[4] = new_standard_deviation
    database_row[7] = count

    # update row in table

    pass


# finds the mean value of all the underlying price
# inputs: current input of product, buyer and seller identifiers
# checks database of estimates and returns its value
def get_underlying_price_estimate(current_product, current_buyer, current_seller):
    # [0] = product name ; [1] = buyer; [2] = seller; [3] mean, [4] standard deviation;
    # [5] = min value; [6] = max value; [7] = count
    database_row = ("3D Maneuver Gears", "XRBV61", "NXTO39", 3500, 250, 300, 4700, 20)

    return database_row
    pass


# function that creates new entry for current product, buyer and seller
# sets the values to their default
def new_underlying_price(c_product, c_buyer, c_seller, current_underlying_price):
    # update table
    max = current_underlying_price
    min = current_underlying_price
    mean = current_underlying_price
    stdev = 0






# function that returns 0 if strike price input is within suggested amount
# returns the estimate value if input is not within bounds
def strike_price_check(current_strike_price):
    current_product = tuple_data.index(2)
    current_buyer = tuple_data.index(3)
    current_seller = tuple_data.index(4)

    if index_check == 0:
        new_notional_estimate()
        return 0
    else:
        estimate = get_notional_estimate(current_product, current_buyer, current_seller)
        mean = estimate[3]
        standard_deviation = estimate[4]
        standard_deviation_multiplier = 5
        standard_deviation_check = standard_deviation_multiplier * standard_deviation
        lower_bound = mean - standard_deviation_check
        higher_bound = mean + standard_deviation_check

        if lower_bound < current_strike_price < higher_bound:
            update_notional_amount(estimate, current_strike_price)
            return 0
        else:
            return estimate


# updates rows in database with new underlying_price estimate
# current row and new notional amount are inputs
def update_strike_price(database_row, current_strike_price):
    # [0] = product name ; [1] = buyer; [2] = seller; [3] mean, [4] standard deviation;
    # [5] = min value; [6] = max value; [7] = count
    count = database_row[7]
    count = count + 1
    old_mean = database_row[3]
    new_mean = ((database_row[3] / count) + current_strike_price) / count

    old_standard_deviation = database_row[4]
    new_standard_deviation = math.sqrt((((count - 2) * (old_standard_deviation ** 2)) + ((count - 1) * ((old_mean - new_mean) ** 2)) + (
            (current_strike_price - new_mean) ** 2)) / (count - 1))

    # update min/max values if necessary
    if current_strike_price < database_row[5]:
        database_row[5] = current_strike_price
    elif current_strike_price > database_row[6]:
        database_row[6] = current_strike_price

    database_row[3] = new_mean
    database_row[4] = new_standard_deviation
    database_row[7] = count

    # update row in table

    pass


# finds the mean value of all the strike price
# inputs: current input of product, buyer and seller identifiers
# checks database of estimates and returns its value
def get_strike_price_estimate(current_product, current_buyer, current_seller):
    # [0] = product name ; [1] = buyer; [2] = seller; [3] mean, [4] standard deviation;
    # [5] = min value; [6] = max value; [7] = count
    database_row = ("3D Maneuver Gears", "XRBV61", "NXTO39", 3500, 250, 300, 4700, 20)

    return database_row
    pass


# function that creates new entry for current product, buyer and seller
# sets the values to their default
def new_strike_price(c_product, c_buyer, c_seller, current_strike_price):
    # update table
    max = current_strike_price
    min = current_strike_price
    mean = current_strike_price
    stdev = 0