import requests
import json
#very experimental api to get data from a stock exchange website and produce data from it depending on inputted request.

#will take an input and put it into the url to be able to request that product -- unsure of how else to approach acquiring real data -- but this method has issue of url may not be formatted correctly therefore request will be denied as for two words e.g. coca cola, it needs to be "coca+cola".
def query(input):
    r = requests.get("https://www.londonstockexchange.com/exchange/prices-and-markets/stocks/prices-search/stock-prices-search.html?nameCode=%s&page=1", input)
    print(r.status_code)
