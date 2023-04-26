#!/usr/bin/python

from ..client import Client
from ..consts import *


class AccountApi(Client):
    def __init__(self, api_key, api_secret_key, passphrase, use_server_time=False, first=False):
        Client.__init__(self, api_key, api_secret_key, passphrase, use_server_time, first)

    def account(self, symbol, marginCoin):
        '''
        ### Obtain user account information
        symbol: Contract transaction pair
        marginCoin: Deposit currency
        :return:
        '''
        params = {}
        if symbol and marginCoin:
            params["symbol"] = symbol
            params["marginCoin"] = marginCoin
            return self._request_with_params(GET, MIX_ACCOUNT_V1_URL + '/account', params)
        else:
            return "pls check args"

    def leverage(self, symbol, marginCoin, leverage, holdSide=''):
        '''
        ### Adjusting lever
        symbol: Contract transaction pair
        marginCoin: Deposit currency
        leverage: Leverage ratio
        holdSide: In the position direction, long multi position short short short positions can not be transferred in case of full positions
        :return:
        '''
        params = {}
        if symbol and marginCoin:
            params["symbol"] = symbol
            params["marginCoin"] = marginCoin
            params["leverage"] = leverage
            params["holdSide"] = holdSide
            return self._request_with_params(POST, MIX_ACCOUNT_V1_URL + '/setLeverage', params)
        else:
            return "pls check args"

    def margin(self, symbol, marginCoin, amount, holdSide=''):
        '''
        ### Adjustment margin
        symbol: Contract transaction pair
        marginCoin: Deposit currency
        amount: Positive increase and negative decrease of deposit amount
        holdSide: In the position direction, long multi position short short short positions can not be transferred in case of full positions
        :return:
        '''
        params = {}
        if symbol and marginCoin:
            params["symbol"] = symbol
            params["marginCoin"] = marginCoin
            params["amount"] = amount
            params["holdSide"] = holdSide
            return self._request_with_params(POST, MIX_ACCOUNT_V1_URL + '/setMargin', params)
        else:
            return "pls check args"

    def margin_mode(self, symbol, marginCoin, marginMode):
        '''
        ### Adjust margin mode
        symbol: Contract transaction pair
        marginCoin: Deposit currency
        marginMode: Fixed warehouse by warehouse crossed full warehouse
        :return:
        '''
        params = {}
        if symbol and marginCoin:
            params["symbol"] = symbol
            params["marginCoin"] = marginCoin
            params["marginMode"] = marginMode
            return self._request_with_params(POST, MIX_ACCOUNT_V1_URL + '/setMarginMode', params)
        else:
            return "pls check args"

    def position_mode(self, symbol, marginCoin, holdMode):
        '''
        ### Set position mode
        symbol: Contract transaction pair
        marginCoin: Deposit currency
        holdMode: Position mode single_ Hold single position double_ Hold Bidirectional Position Default Bidirectional Position
        :return:
        '''
        params = {}
        if symbol and marginCoin and holdMode:
            params["symbol"] = symbol
            params["marginCoin"] = marginCoin
            params["holdMode"] = holdMode
            return self._request_with_params(POST, MIX_ACCOUNT_V1_URL + '/setPositionMode', params)
        else:
            return "pls check args"

    def open_count(self, symbol, marginCoin, openPrice, openAmount, leverage=20):
        '''
        ### Query the number of open sheets
        symbol: Contract transaction pair
        marginCoin: Deposit currency
        openPrice： Opening price
        openAmount: Opening limit
        leverage: Default leverage 20
        :return:
        '''
        params = {}
        if symbol and marginCoin and openPrice and openAmount:
            params["symbol"] = symbol
            params["marginCoin"] = marginCoin
            params["openPrice"] = openPrice
            params["openAmount"] = openAmount
            params["leverage"] = leverage
            return self._request_with_params(POST, MIX_ACCOUNT_V1_URL + '/open-count', params)
        else:
            return "pls check args"

    def accounts(self, productType):
        '''
        ### Get account information list
        productType: Umcbl (USDT professional contract) dmcbl (mixed contract) sumcbl (USDT professional contract simulation disk) sdmcbl (mixed contract simulation disk)
        :return:
        '''
        params = {}
        if productType:
            params['productType'] = productType
            return self._request_with_params(GET, MIX_ACCOUNT_V1_URL + '/accounts', params)
        else:
            return "pls check args"

    def accountBill(self, symbol,marginCoin,startTime,endTime,lastEndId = '',pageSize=20,next=False):
        '''
        ### Obtain the list of account flow information
        :return:
        '''
        params = {}
        if symbol and marginCoin and startTime and endTime:
            params['symbol'] = symbol
            params['marginCoin'] = marginCoin
            params['startTime'] = startTime
            params['endTime'] = endTime
            params['lastEndId'] = lastEndId
            params['pageSize'] = pageSize
            params['next'] = next
            return self._request_with_params(GET, MIX_ACCOUNT_V1_URL + '/accountBill', params)
        else:
            return "pls check args"
