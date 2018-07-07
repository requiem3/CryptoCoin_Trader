from binance.client import Client
from decimal import *


class BinanceReader:
    # DELETE KEYS BEFORE PUSHING REEEEEEEEEEEEEEE
    # DELETE KEYS BEFORE PUSHING REEEEEEEEEEEEEEE
    # DELETE KEYS BEFORE PUSHING REEEEEEEEEEEEEEE
    # DELETE KEYS BEFORE PUSHING REEEEEEEEEEEEEEE
    # DELETE KEYS BEFORE PUSHING REEEEEEEEEEEEEEE
    API_KEY = ""
    SECRET = ""

    def __init__(self):
        self.client = Client(self.API_KEY, self.SECRET)

    """
    returns a list off all symbols in the exchange IE. LTCBTC
    """
    def getAllSymbols(self):
        info = self.client.get_exchange_info()
        symbolList = []
        for x in info['symbols']:
            symbolList.append(x['symbol'])
        return symbolList

    """
    returns the 24hr volume traded
    :param s: symbol IE 'LTCBTC'
    """
    def getDailyVolume(self, s):
        return self.client.get_ticker(symbol=s)['volume']

    """
    retuns how many are traded in a given second window
    """
    def calcSecondWindow(self,window,dailyVolume):
        return dailyVolume/(86400/window)

    """
    returns the profit value
    :param s: symbol IE 'LYCBTC'
    """
    def getProfitWindow(self, s):
        depth = self.client.get_order_book(symbol=s)
        c1 = Decimal(depth["asks"][0][0]) * Decimal(.001)
        c2 = Decimal(depth["bids"][0][0]) * Decimal(.001)
        profit = (Decimal(depth["asks"][0][0]) - c1) - (Decimal(depth["bids"][0][0]) + c2)
        return profit
