#!/usr/bin/python

from ..client import Client
from ..consts import *


class PositionApi(Client):
    def __init__(
        self,
        api_key: str,
        api_secret_key: str,
        passphrase: str,
        use_server_time: bool = False,
        first: bool = False,
    ):
        """
        ### PositionApi class is connect to account interface :
        https://bitgetlimited.github.io/apidoc/zh/mix/#f1e69afa43
        api_key: API key
        api_secret_key: API secret key
        passphrase: API passphrase
        use_server_time: Use Bitget server time
        first: Check url, method, body and header
        """
        Client.__init__(
            self, api_key, api_secret_key, passphrase, use_server_time, first
        )

    def singlePosition(self, symbol: str, marginCoin: str):
        """
        ### Obtain the user's single position information
        symbol: Contract transaction pair, ex: "BTCUSDT_UMCBL"
        marginCoin: Deposit currency, ex: "USDT"
        """
        params = {}
        if symbol and marginCoin:
            params["symbol"] = symbol
            params["marginCoin"] = marginCoin
            return self._request_with_params(
                GET, MIX_POSITION_V1_URL + "/singlePosition", params
            )
        else:
            return "pls check args"

    def allPosition(self, productType: str, marginCoin: str = ""):
        """
        ### Obtain all position information of the user
        productType: Contract transaction pair productType, ex: "umcbl"
        marginCoin: Deposit currency, ex: "USDT"
        """
        params = {}
        if productType:
            params["productType"] = productType
            params["marginCoin"] = marginCoin
            return self._request_with_params(
                GET, MIX_POSITION_V1_URL + "/allPosition", params
            )
        else:
            return "pls check args"

    def history_position(
        self,
        startTime: str,
        endTime: str,
        productType: str = "",
        symbol: str = "",
        pageSize: str = "",
        lastEndId: str = "",
    ):
        """
        ### Obtain history position information of the user ("productType" or "symbol" must be passed one)
        startTime: Bill start timestamp, ex: "1659403328000"
        endTime: Bill end timestamp, ex: "1659406928000"
        productType: Contract transaction pair productType, ex: "umcbl"
        symbol: Contract transaction pair, ex: "BTCUSDT_UMCBL"
        pageSize: Illustrate page size, ex: "20", "50"
        lastEndId: Last Id of account bill, ex: "1076451359571689476"
        """
        params = {}
        if startTime and endTime and (productType or symbol):
            params["startTime"] = startTime
            params["endTime"] = endTime
            params["productType"] = productType
            params["symbol"] = symbol
            params["pageSize"] = pageSize
            params["lastEndId"] = lastEndId
            return self._request_with_params(
                GET, MIX_POSITION_V1_URL + "/history-position", params
            )
        else:
            return "pls check args"
