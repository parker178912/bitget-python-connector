#!/usr/bin/python

from ..client import Client
from ..consts import *


class MarketApi(Client):
    def __init__(self, api_key, api_secret_key, passphrase, use_server_time=False, first=False):
        Client.__init__(self, api_key, api_secret_key, passphrase, use_server_time, first)

    def contracts(self, productType):
        '''
        ### Get contract list
        productType: Umcbl (USDT professional contract) dmcbl (mixed contract) sumcbl (USDT professional contract simulation disk) sdmcbl (mixed contract simulation disk)
        :return:
        '''
        params = {}
        if productType:
            params['productType'] = productType
        return self._request_with_params(GET, MIX_MARKET_V1_URL + '/contracts', params)

    def depth(self, symbol, limit='150'):
        '''
        ### Get depth data
        symbol：Contract transaction pair
        :return:
        '''
        params = {}
        if symbol and limit and type:
            params["symbol"] = symbol
            params["limit"] = limit
            return self._request_with_params(GET, MIX_MARKET_V1_URL + '/depth', params)
        else:
            return "pls check args"

    def ticker(self, symbol):
        '''
        ### Get ticker information according to the currency pair
        symbol：Contract transaction pair
        :return:
        '''
        params = {}
        if symbol:
            params["symbol"] = symbol
            return self._request_with_params(GET, MIX_MARKET_V1_URL + '/ticker', params)
        else:
            return "pls check args"

    def tickers(self,productType):
        '''
        ### Get all ticket information
        productType: Umcbl (USDT professional contract) dmcbl (mixed contract) sumcbl (USDT professional contract simulation disk) sdmcbl (mixed contract simulation disk)
        :return:
        '''
        params = {}
        if productType:
            params['productType'] = productType
        return self._request_with_params(GET, MIX_MARKET_V1_URL + '/tickers', params)

    def fills(self, symbol, limit=100):
        '''
        ### Get real-time transaction
        symbol：Contract transaction pair
        :return:
        '''
        params = {}
        if symbol and limit:
            params["symbol"] = symbol
            params["limit"] = limit
            return self._request_with_params(GET, MIX_MARKET_V1_URL + '/fills', params)
        else:
            return "pls check args"

    def candles(self, symbol, granularity, startTime='', endTime='',limit=''):
        '''
        ### Obtain K line information
        params
        period: 60, 300, 900, 1800, 3600,14400,43200, 86400, 604800
        startTime: start time
        endTime: end time
        :return:
        '''
        params = {}
        if symbol and granularity:
            params["symbol"] = symbol
            params["granularity"] = granularity
            params["startTime"] = startTime
            params["endTime"] = endTime
            params["limit"] = limit
            return self._request_with_params(GET, MIX_MARKET_V1_URL + '/candles', params)
        else:
            return "pls check args"

    def index(self, symbol):
        '''
        ### Currency index price
        symbol：Contract transaction pair
        :return:
        '''
        params = {}
        if symbol:
            params["symbol"] = symbol
            return self._request_with_params(GET, MIX_MARKET_V1_URL + '/index', params)
        else:
            return "pls check args"

    def funding_time(self, symbol):
        '''
        ### Next settlement time
        symbol：Contract transaction pair
        :return:
        '''
        params = {}
        if symbol:
            params["symbol"] = symbol
            return self._request_with_params(GET, MIX_MARKET_V1_URL + '/funding-time', params)
        else:
            return "pls check args"

    def market_price(self, symbol):
        '''
        ### Contract Mark Price
        symbol：Contract transaction pair
        :return:
        '''
        params = {}
        if symbol:
            params["symbol"] = symbol
            return self._request_with_params(GET, MIX_MARKET_V1_URL + '/mark-price', params)
        else:
            return "pls check args"

    def history_fund_rate(self, symbol, pageSize=20, pageNo=1, nextPage=False):
        '''
        ### Historical fund rate
        symbol：Contract transaction pair
        pageSize: Number of queries
        pageNo: Number of query pages
        nextPage: Whether to query the next page
        :return:F
        '''
        params = {}
        if symbol:
            params["symbol"] = symbol
            params["pageSize"] = pageSize
            params["pageNo"] = pageNo
            params["nextPage"] = nextPage
            return self._request_with_params(GET, MIX_MARKET_V1_URL + '/history-fundRate', params)
        else:
            return "pls check args"

    def current_fund_rate(self, symbol):
        '''
        ### Current fund rate
        symbol：Contract transaction pair
        :return:F
        '''
        params = {}
        if symbol:
            params["symbol"] = symbol
            return self._request_with_params(GET, MIX_MARKET_V1_URL + '/current-fundRate', params)
        else:
            return "pls check args"

    def open_interest(self, symbol):
        '''
        ### Obtain the total position of the platform
        symbol：Contract transaction pair
        :return:
        '''
        params = {}
        if symbol:
            params["symbol"] = symbol
            return self._request_with_params(GET, MIX_MARKET_V1_URL + '/open-interest', params)
        else:
            return "pls check args"
