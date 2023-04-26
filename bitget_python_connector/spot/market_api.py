#!/usr/bin/python

from ..client import Client
from ..consts import *


class MarketApi(Client):

    def __init__(self, api_key, api_secret_key, passphrase, use_server_time=False, first=False):
        Client.__init__(self, api_key, api_secret_key, passphrase, use_server_time, first)

    def fills(self, symbol, limit=100):
        '''
        ### Get real-time transaction
        :return:
        '''
        params = {}
        if symbol and limit:
            params["symbol"] = symbol
            params["limit"] = limit
            return self._request_with_params(GET, SPOT_MARKET_V1_URL + '/fills', params)
        else:
            return "pls check args"

    def depth(self, symbol, limit='150', type='step0'):
        '''
        ### Get depth data
        Depth Merge Type
        type: step0(default) step1 step2 step3 step4 step5
        :return:
        '''
        params = {}
        if symbol and limit and type:
            params["symbol"] = symbol
            params["limit"] = limit
            params["type"] = type
            return self._request_with_params(GET, SPOT_MARKET_V1_URL + '/depth', params)
        else:
            return "pls check args"

    def ticker(self, symbol):
        '''
        ### Get ticker information according to the currency pair
        :return:
        '''
        params = {}
        if symbol:
            params["symbol"] = symbol
            return self._request_with_params(GET, SPOT_MARKET_V1_URL + '/ticker', params)
        else:
            return "pls check args"


    def tickers(self):
        '''
        ### Get all transaction pair ticker information
        :return:
        '''
        return self._request_without_params(GET, SPOT_MARKET_V1_URL + '/tickers')

    def candles(self, symbol, period, after='', before='', limit=100):
        '''
        ### Obtain K line information
        params
        
        period: 1min, 5min, 15min, 30min, 1h,4h,12h, 1day, 1week
        after: time before
        before: time after
        :return:
        '''
        params = {}
        if symbol and period:
            params["symbol"] = symbol
            params["period"] = period
            params["after"] = after
            params["before"] = before
            params["limit"] = limit
            return self._request_with_params(GET, SPOT_MARKET_V1_URL + '/candles', params)
        else:
            return "pls check args"