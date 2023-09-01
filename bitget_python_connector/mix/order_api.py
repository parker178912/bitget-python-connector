#!/usr/bin/python

from ..client import Client
from ..consts import *


class OrderApi(Client):
    def __init__(
        self,
        api_key: str,
        api_secret_key: str,
        passphrase: str,
        use_server_time: bool = False,
        first: bool = False,
    ):
        """
        ### OrderApi class is connect to account interface :
        https://bitgetlimited.github.io/apidoc/zh/mix/#fd6ce2a756
        api_key: API key
        api_secret_key: API secret key
        passphrase: API passphrase
        use_server_time: Use Bitget server time
        first: Check url, method, body and header
        """
        Client.__init__(
            self, api_key, api_secret_key, passphrase, use_server_time, first
        )

    def placeOrder(
        self,
        symbol: str,
        marginCoin: str,
        size: str,
        side: str,
        orderType: str,
        clientOrderId: str = "",
        price: str = "",
        timeInForceValue: str = "normal",
        reduceOnly: bool = False,
        presetTakeProfitPrice: str = "",
        presetStopLossPrice: str = "",
    ):
        """
        ### Place an order
        symbol: Contract transaction pair, ex: "BTCUSDT_UMCBL"
        marginCoin: Deposit currency, ex: "USDT"
        size: Quantity of opening size, ex: "0.1", "0.05"
        side: Order action, ex: "open_long", "open_short", "close_long", "close_short"
        orderType: Order in fixed or marker price, ex: "limit", "market"
        clientOrderId: Client specific order id, ex: "123456"
        price: Price limit for "fixed" orderType, ex: "1951.32"
        timeInForceValue: Order validity period, ex: "normal", "postOnly"
        reduceOnly: Only decrease order, ex: False, True
        presetTakeProfitPrice: Default stop profit price, ex: "1945.32"
        presetStopLossPrice: Preset stop loss price, ex: "1960.32"
        """
        params = {}
        if symbol and marginCoin and side and orderType:
            params["symbol"] = symbol
            params["marginCoin"] = marginCoin
            params["price"] = price
            params["size"] = size
            params["side"] = side
            params["orderType"] = orderType
            params["timeInForceValue"] = timeInForceValue
            params["clientOid"] = clientOrderId
            params["reduceOnly"] = reduceOnly
            params["presetTakeProfitPrice"] = presetTakeProfitPrice
            params["presetStopLossPrice"] = presetStopLossPrice
            return self._request_with_params(
                POST, MIX_ORDER_V1_URL + "/placeOrder", params
            )
        else:
            return "pls check args "

    def batch_orders(self, symbol: str, marginCoin: str, orderDataList: list[dict]):
        """
        ### Place orders in batches
        symbol: Contract transaction pair, ex: "BTCUSDT_UMCBL"
        marginCoin: Deposit currency, ex: "USDT"
        orderDataList:
            size: Quantity of opening size, ex: "0.1", "0.05"
            side: Order action, ex: "open_long", "open_short", "close_long", "close_short"
            orderType: Order in fixed or marker price, ex: "limit", "market"
            clientOrderId: Client specific order id, ex: "123456"
            price: Price limit for "fixed" orderType, ex: "1951.32"
            timeInForceValue: Order validity period, ex: "normal", "postOnly"
            presetTakeProfitPrice: Default stop profit price, ex: "1945.32"
            presetStopLossPrice: Preset stop loss price, ex: "1960.32"
        """
        params = {
            "symbol": symbol,
            "marginCoin": marginCoin,
            "orderDataList": orderDataList,
        }
        return self._request_with_params(
            POST, MIX_ORDER_V1_URL + "/batch-orders", params
        )

    def cancel_orders(
        self, symbol: str, marginCoin: str, orderId: str = "", clientOid: str = ""
    ):
        """
        ### Cancel order ('orderId' or 'clientOid' must provide one)
        symbol: Contract transaction pair, ex: "BTCUSDT_UMCBL"
        marginCoin: Deposit currency, ex: "USDT"
        orderId: Specific order id, ex: "1077085840431235088"
        clientOid: Client specific order id, ex: "123456"
        """
        params = {}
        if symbol and marginCoin and (orderId or clientOid):
            params["symbol"] = symbol
            params["marginCoin"] = marginCoin
            if orderId:
                params["orderId"] = orderId
            elif clientOid:
                params["clientOid"] = clientOid
            return self._request_with_params(
                POST, MIX_ORDER_V1_URL + "/cancel-order", params
            )
        else:
            return "pls check args "

    def cancel_batch_orders(
        self, symbol: str, marginCoin: str, orderIds: list = [], clientOids: list = []
    ):
        """
        ### Batch cancellation
        symbol: Contract transaction pair, ex: "BTCUSDT_UMCBL"
        marginCoin: Deposit currency, ex: "USDT"\\
        orderIds ('orderIds' or 'clientOids' must provide one) :
            orderIds: Specific order id list, ex: "1077085840431235088"
            clientOids: Client specific order id list, ex: "123456"   
        """
        if symbol and marginCoin and (orderIds or clientOids):
            params = {
                "symbol": symbol,
                "marginCoin": marginCoin,
                "orderIds": orderIds,
                "clientOids": clientOids,
            }
            return self._request_with_params(
                POST, MIX_ORDER_V1_URL + "/cancel-batch-orders", params
            )
        else:
            return "pls check args "

    def modifyOrder(
        self,
        symbol: str,
        orderId: str = "",
        clientOid: str = "",
        newClientOid: str = "",
        size: str = "",
        price: str = "",
        presetTakeProfitPrice: str = "",
        presetStopLossPrice: str = "",
    ):
        """
        ### Modify specific order ('orderId' or 'clientOid' must provide one)
        symbol: Contract transaction pair, ex: "BTCUSDT_UMCBL"
        orderId: Specific order id, ex: "1077085840431235088"
        clientOid: Client specific order id, ex: "123456"
        newClientOid: New specific order id, ex: "44848643"
        size: Quantity of opening size, ex: "0.1", "0.05"
        price: Price limit for "fixed" orderType, ex: "1951.32"
        presetTakeProfitPrice: Default stop profit price, ex: "1945.32"
        presetStopLossPrice: Preset stop loss price, ex: "1960.32"
        """
        params = {}
        if symbol and (orderId or clientOid):
            params["symbol"] = symbol
            params["orderId"] = orderId
            params["clientOid"] = clientOid
            params["newClientOid"] = newClientOid
            params["size"] = size
            params["price"] = price
            params["presetTakeProfitPrice"] = presetTakeProfitPrice
            params["presetStopLossPrice"] = presetStopLossPrice
            return self._request_with_params(
                POST, MIX_ORDER_V1_URL + "/modifyOrder", params
            )
        else:
            return "pls check args "

    def cancel_symbol_orders(self, symbol: str, marginCoin: str):
        """
        ### Cancel all order of symbol
        symbol: Contract transaction pair, ex: "BTCUSDT_UMCBL"
        marginCoin: Deposit currency, ex: "USDT"
        """
        params = {}
        if symbol and marginCoin:
            params["symbol"] = symbol
            params["marginCoin"] = marginCoin
            return self._request_with_params(
                POST, MIX_ORDER_V1_URL + "/cancel-symbol-orders", params
            )
        else:
            return "pls check args "

    def cancel_all_orders(self, productType: str, marginCoin: str):
        """
        ### Cancel all order
        productType: Contract transaction pair productType, ex: "umcbl"
        marginCoin: Deposit currency, ex: "USDT"
        """
        params = {}
        if productType and marginCoin:
            params["productType"] = productType
            params["marginCoin"] = marginCoin
            return self._request_with_params(
                POST, MIX_ORDER_V1_URL + "/cancel-all-orders", params
            )
        else:
            return "pls check args "

    def cancel_all_positions(self, productType: str):
        """
        ### Cancel all positions
        productType: Contract transaction pair productType, ex: "umcbl"
        """
        params = {}
        if productType:
            params["productType"] = productType
            return self._request_with_params(
                POST, MIX_ORDER_V1_URL + "/close-all-positions", params
            )
        else:
            return "pls check args "

    def current(self, symbol: str):
        """
        ### Get the current order
        symbol: Contract transaction pair, ex: "BTCUSDT_UMCBL"
        """
        params = {}
        if symbol:
            params["symbol"] = symbol
            return self._request_with_params(GET, MIX_ORDER_V1_URL + "/current", params)
        else:
            return "pls check args "

    def marginCoinCurrent(self, productType: str, marginCoin: str):
        """
        ### Get all orders
        productType: Contract transaction pair productType, ex: "umcbl"
        marginCoin: Deposit currency, ex: "USDT"
        """
        params = {}
        if productType and marginCoin:
            params["productType"] = productType
            params["marginCoin"] = marginCoin
            return self._request_with_params(
                GET, MIX_ORDER_V1_URL + "/marginCoinCurrent", params
            )
        else:
            return "pls check args "

    def historyProductType(
        self,
        productType: str,
        startTime: str,
        endTime: str,
        pageSize: str,
        lastEndId: str = "",
        clientOid: str = "",
        isPre: bool = False,
    ):
        """
        ### Get Historical Delegation
        productType: Contract transaction pair productType, ex: "umcbl"
        startTime: Bill start timestamp, ex: "1659403328000"
        endTime: Bill end timestamp, ex: "1659406928000"
        pageSize: Illustrate page size, ex: "20", "50"
        lastEndId: Last Id of account bill, ex: "1076451359571689476"
        clientOid: Client specific order id, ex: "123456"
        isPre: Whether to query the previous page, ex: False, True
        """
        params = {}
        if productType and startTime and endTime and pageSize:
            params["productType"] = productType
            params["startTime"] = startTime
            params["endTime"] = endTime
            params["pageSize"] = pageSize
            params["lastEndId"] = lastEndId
            params["clientOid"] = clientOid
            params["isPre"] = isPre
            return self._request_with_params(
                GET, MIX_ORDER_V1_URL + "/historyProductType", params
            )
        else:
            return "pls check args "

    def detail(self, symbol: str, orderId: str = "", clientOid: str = ""):
        """
        ### Get order information ('orderId' or 'clientOid' must provide one)
        symbol: Contract transaction pair, ex: "BTCUSDT_UMCBL"
        orderId: Specific order id, ex: "1077085840431235088"
        clientOid: Client specific order id, ex: "123456"
        """
        params = {}
        if symbol and (orderId or clientOid):
            params["symbol"] = symbol
            params["orderId"] = orderId
            params["clientOid"] = clientOid
            return self._request_with_params(GET, MIX_ORDER_V1_URL + "/detail", params)
        else:
            return "pls check args "

    def fills(
        self,
        symbol: str,
        orderId: str = "",
        startTime: str = "",
        endTime: str = "",
        lastEndId: str = "",
    ):
        """
        ### Obtain transaction details
        symbol: Contract transaction pair, ex: "BTCUSDT_UMCBL"
        orderId: Specific order id, ex: "1077085840431235088"
        startTime: Bill start timestamp, ex: "1659403328000"
        endTime: Bill end timestamp, ex: "1659406928000"
        lastEndId: Last Id of account bill, ex: "1076451359571689476"
        """
        params = {}
        if symbol and (orderId or (startTime and endTime)):
            params["symbol"] = symbol
            params["orderId"] = orderId
            params["startTime"] = startTime
            params["endTime"] = endTime
            params["lastEndId"] = lastEndId
            return self._request_with_params(GET, MIX_ORDER_V1_URL + "/fills", params)
        else:
            return "pls check args "

    def allFills(
        self, productType: str, startTime: str, endTime: str, lastEndId: str = ""
    ):
        """
        ### Obtain all transaction details
        productType: Contract transaction pair productType, ex: "umcbl"
        startTime: Bill start timestamp, ex: "1659403328000"
        endTime: Bill end timestamp, ex: "1659406928000"
        lastEndId: Last Id of account bill, ex: "1076451359571689476"
        """
        params = {}
        if productType and startTime and endTime:
            params["productType"] = productType
            params["startTime"] = startTime
            params["endTime"] = endTime
            params["lastEndId"] = lastEndId
            return self._request_with_params(
                GET, MIX_ORDER_V1_URL + "/allFills", params
            )
        else:
            return "pls check args "
