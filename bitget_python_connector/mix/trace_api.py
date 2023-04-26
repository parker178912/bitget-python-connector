#!/usr/bin/python

from ..client import Client
from ..consts import *


class TraceApi(Client):
    def __init__(self, api_key, api_secret_key, passphrase, use_server_time=False, first=False):
        Client.__init__(self, api_key, api_secret_key, passphrase, use_server_time, first)

    def close_track_order(self, symbol, trackingNo):
        '''
        ### Dealers close positions
        symbol： Trading pair name
        trackingNo: Tracking order No
        :return:
        '''
        params = {}
        if symbol and trackingNo:
            params["symbol"] = symbol
            params["trackingNo"] = trackingNo
            return self._request_with_params(POST, MIX_TRACE_V1_URL + '/closeTrackOrder', params)
        else:
            return "pls check args "

    def current_track(self, symbol, productType, pageSize=20, pageNo=1):
        '''
        ### The trader obtains the current order
        symbol: Trading pair name
        productType: Umcbl (USDT professional contract) dmcbl (mixed contract) sumcbl (USDT professional contract simulation disk) sdmcbl (mixed contract simulation disk)
        pageNo： Start at 1
        :return:
        '''
        params = {}
        if symbol:
            params["symbol"] = symbol
            params["productType"] = productType
            params["pageSize"] = pageSize
            params["pageNo"] = pageNo
            return self._request_with_params(GET, MIX_TRACE_V1_URL + '/currentTrack', params)
        else:
            return "pls check args "

    def history_track(self, startTime, endTime, pageSize=100, pageNo=1):
        '''
        ### The trader obtains the current order
        symbol: Trading pair name
        startTime: start time
        endTime: end time
        pageSize: Number of queries
        pageNo: Number of query pages
        :return:
        '''
        params = {}
        if startTime and endTime:
            params["startTime"] = startTime
            params["endTime"] = endTime
            params["pageSize"] = pageSize
            params["pageNo"] = pageNo
            return self._request_with_params(GET, MIX_TRACE_V1_URL + '/historyTrack', params)
        else:
            return "pls check args "

    def summary(self):
        '''
        ### Summary of traders' profit sharing
        :return:
        '''
        return self._request_without_params(GET, MIX_TRACE_V1_URL + '/summary')

    def profit_settle_margin_coin(self):
        '''
        ### Summary of traders' profit sharing (by settlement currency)
        :return:
        '''
        return self._request_without_params(GET, MIX_TRACE_V1_URL + '/profitSettleTokenIdGroup')

    def profit_date_group(self, pageSize, pageNo):
        '''
        ### Summary of traders' profit sharing (by date)
        :return:
        '''
        params = {}
        if pageSize and pageNo:
            params["pageSize"] = pageSize
            params["pageNo"] = pageNo
            return self._request_with_params(GET, MIX_TRACE_V1_URL + '/profitDateGroupList', params)
        else:
            return "pls check args "

    def profit_date_detail(self, marginCoin, date, pageSize, pageNo):
        '''
        ### Historical profit distribution details of traders
        :return:
        '''
        params = {}
        if marginCoin and date and pageSize and pageNo:
            params["marginCoin"] = marginCoin
            params["date"] = date
            params["pageSize"] = pageSize
            params["pageNo"] = pageNo
            return self._request_with_params(GET, MIX_TRACE_V1_URL + '/profitDateList', params)
        else:
            return "pls check args "

    def wait_profit_detail(self, pageSize, pageNo):
        '''
        ### Details of traders to be distributed
        :return:
        '''
        params = {}
        if pageSize and pageNo:
            params["pageSize"] = pageSize
            params["pageNo"] = pageNo
            return self._request_with_params(GET, MIX_TRACE_V1_URL + '/waitProfitDateList', params)
        else:
            return "pls check args "

    def follower_history_orders(self, page_size, page_no, start_time, end_time):
        '''
        ### Followers obtain information on opening and closing orders
        :return:
        '''
        params = {}
        if page_size and page_no:
            params["pageSize"] = page_size
            params["pageNo"] = page_no

        if start_time and end_time:
            params["startTime"] = start_time
            params["endTime"] = end_time

        return self._request_with_params(GET, MIX_TRACE_V1_URL + '/followerHistoryOrders', params)

    def trader_symbols(self):
        '''
        ### Get trader copytrader symbol
        '''
        return self._request_without_params(GET, MIX_TRACE_V1_URL + '/traderSymbols')

    def set_trder_symbol(self, symbol):
        '''
        ### Set trader copytrader symbol
        '''
        params = {}
        if symbol:
            params["symbol"] = symbol
            return self._request_with_params(POST, MIX_TRACE_V1_URL + '/setUpCopySymbols', params)
        else:
            return "pls check args "

    def trader_modify_tpsl_order(self, symbol, trackingNo, stopProfitPrice, stopLossPrice):
        '''
        ### Trader modify tpsl order
        '''
        params = {}
        if symbol and trackingNo:
            params["symbol"] = symbol
            params["trackingNo"] = trackingNo
            params["stopProfitPrice"] = stopProfitPrice
            params["stopLossPrice"] = stopLossPrice
            return self._request_with_params(POST, MIX_TRACE_V1_URL + '/modifyTPSL', params)
        else:
            return "pls check args "

    def followerOrder(self, symbol, productType, pageSize=100, pageNo=1):
        '''
        ### FollowerOrder
        '''
        params = {}
        if symbol and productType:
            params["symbol"] = symbol
            params["productType"] = productType
            params["pageSize"] = pageSize
            params["pageNo"] = pageNo
            return self._request_with_params(GET, MIX_TRACE_V1_URL + '/followerOrder', params)
        else:
            return "pls check args "
