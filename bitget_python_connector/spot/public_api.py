#!/usr/bin/python

from ..client import Client
from ..consts import *


class PublicApi(Client):

    def __init__(self, api_key, api_secret_key, passphrase, use_server_time=False, first=False):
        Client.__init__(self, api_key, api_secret_key, passphrase, use_server_time, first)

    def times(self):
        '''
        Get Timestamp
        :return:
        '''
        return self._request_without_params(GET, SPOT_PUBLIC_V1_URL + '/time')

    def currencies(self):
        '''
        Get all currencies
        :return:
        '''
        return self._request_without_params(GET, SPOT_PUBLIC_V1_URL + '/currencies')

    def products(self):
        '''
        Get all transaction pair information
        :return:
        '''
        return self._request_without_params(GET, SPOT_PUBLIC_V1_URL+'/products')

    def product(self, symbol):
        '''
        Obtain single currency pair information according to the transaction pair
        :return:
        '''
        params = {}
        if symbol:
            params["symbol"] = symbol
            return self._request_with_params(GET, SPOT_PUBLIC_V1_URL+'/product', params)
        else:
            return "pls check args"



