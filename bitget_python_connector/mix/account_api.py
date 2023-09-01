#!/usr/bin/python

from ..client import Client
from ..consts import *


class AccountApi(Client):
    def __init__(
        self,
        api_key: str,
        api_secret_key: str,
        passphrase: str,
        use_server_time: bool = False,
        first: bool = False,
    ):
        """
        ### AccountApi class is connect to account interface :
        https://bitgetlimited.github.io/apidoc/zh/mix/#df03e301d5
        api_key: API key
        api_secret_key: API secret key
        passphrase: API passphrase
        use_server_time: Use Bitget server time
        first: Check url, method, body and header
        """
        Client.__init__(
            self, api_key, api_secret_key, passphrase, use_server_time, first
        )

    def account(self, symbol: str, marginCoin: str):
        """
        ### Obtain user account information
        symbol: Contract transaction pair, ex: "BTCUSDT_UMCBL"
        marginCoin: Deposit currency, ex: "USDT"
        """
        params = {}
        if symbol and marginCoin:
            params["symbol"] = symbol
            params["marginCoin"] = marginCoin
            return self._request_with_params(
                GET, MIX_ACCOUNT_V1_URL + "/account", params
            )
        else:
            return "pls check args"

    def accounts(self, productType: str):
        """
        ### Get account information list
        productType: Contract transaction pair productType, ex: "umcbl"
        """
        params = {}
        if productType:
            params["productType"] = productType
            return self._request_with_params(
                GET, MIX_ACCOUNT_V1_URL + "/accounts", params
            )
        else:
            return "pls check args"

    def sub_account_contract_assets(self, productType: str):
        """
        ### Get all subaccount asset information
        productType: Contract transaction pair productType, ex: "umcbl"
        """
        params = {}
        if productType:
            params["productType"] = productType
            return self._request_with_params(
                POST, MIX_ACCOUNT_V1_URL + "/sub-account-contract-assets", params
            )
        else:
            return "pls check args"

    def open_count(
        self,
        symbol: str,
        marginCoin: str,
        openPrice: str | float | int,
        openAmount: str | float | int,
        leverage: int = 20,
    ):
        """
        ### Query the number of open sheets
        symbol: Contract transaction pair, ex: "BTCUSDT_UMCBL"
        marginCoin: Deposit currency, ex: "USDT"\\
        openPrice： Opening price, ex: "23189.5"
        openAmount: Opening limit, ex: "5000"
        leverage: Default leverage 20, ex: "50"
        """
        params = {}
        if symbol and marginCoin and openPrice and openAmount:
            params["symbol"] = symbol
            params["marginCoin"] = marginCoin
            params["openPrice"] = openPrice
            params["openAmount"] = openAmount
            params["leverage"] = leverage
            return self._request_with_params(
                POST, MIX_ACCOUNT_V1_URL + "/open-count", params
            )
        else:
            return "pls check args"

    def setLeverage(
        self, symbol: str, marginCoin: str, leverage: str, holdSide: str = ""
    ):
        """
        ### Adjusting levererage
        symbol: Contract transaction pair, ex: "BTCUSDT_UMCBL"
        marginCoin: Deposit currency, ex: "USDT"
        leverage: Leverage ratio, ex: "20"
        holdSide: Position side (only send in fixed margin), ex: "long", "short"
        """
        params = {}
        if symbol and marginCoin:
            params["symbol"] = symbol
            params["marginCoin"] = marginCoin
            params["leverage"] = leverage
            params["holdSide"] = holdSide
            return self._request_with_params(
                POST, MIX_ACCOUNT_V1_URL + "/setLeverage", params
            )
        else:
            return "pls check args"

    def setMargin(self, symbol: str, marginCoin: str, amount: str, holdSide: str = ""):
        """
        ### Adjustment margin
        symbol: Contract transaction pair, ex: "BTCUSDT_UMCBL"
        marginCoin: Deposit currency, ex: "USDT"
        amount: Positive increase and negative decrease of deposit amount, ex: "10", "-10"
        holdSide: Position side (only send in fixed margin), ex: "long", "short"
        """
        params = {}
        if symbol and marginCoin:
            params["symbol"] = symbol
            params["marginCoin"] = marginCoin
            params["amount"] = amount
            params["holdSide"] = holdSide
            return self._request_with_params(
                POST, MIX_ACCOUNT_V1_URL + "/setMargin", params
            )
        else:
            return "pls check args"

    def setMarginMode(self, symbol: str, marginCoin: str, marginMode: str):
        """
        ### Adjust margin mode
        symbol: Contract transaction pair, ex: "BTCUSDT_UMCBL"
        marginCoin: Deposit currency, ex: "USDT"
        marginMode: Postion marginMode, ex: "crossed", "fixed"
        """
        params = {}
        if symbol and marginCoin:
            params["symbol"] = symbol
            params["marginCoin"] = marginCoin
            params["marginMode"] = marginMode
            return self._request_with_params(
                POST, MIX_ACCOUNT_V1_URL + "/setMarginMode", params
            )
        else:
            return "pls check args"

    def setPositionMode(self, productType: str, holdMode: str):
        """
        ### Set position mode (All transaction pair)
        productType: Contract transaction pair productType, ex: "umcbl"
        holdMode: Position holdMod, ex: "single_hold", "double_hold"
        """
        params = {}
        if productType and holdMode:
            params["productType"] = productType
            params["holdMode"] = holdMode
            return self._request_with_params(
                POST, MIX_ACCOUNT_V1_URL + "/setPositionMode", params
            )
        else:
            return "pls check args"

    def accountBill(
        self,
        productType: str,
        marginCoin: str,
        startTime: str,
        endTime: str,
        business: str = "",
        pageSize: int = 20,
        lastEndId: str = "",
    ):
        """
        ### Obtain the list of account flow information
        productType: Contract transaction pair productType, ex: "umcbl"
        marginCoin: Deposit currency, ex: "USDT"
        startTime: Bill start timestamp, ex: "1659403328000"
        endTime: Bill end timestamp, ex: "1659406928000"
        business: Business type, ex: "open_long", "open_short"
        pageSize: Illustrate page size, ex: 20, 50
        lastEndId: Last Id of account bill, ex: "1076451359571689476"
        """
        params = {}
        if productType and marginCoin and startTime and endTime:
            params["productType"] = productType
            params["marginCoin"] = marginCoin
            params["startTime"] = startTime
            params["endTime"] = endTime
            params["business"] = business
            params["lastEndId"] = lastEndId
            params["pageSize"] = pageSize
            return self._request_with_params(
                GET, MIX_ACCOUNT_V1_URL + "/accountBill", params
            )
        else:
            return "pls check args"

    def accountBusinessBill(
        self,
        productType: str,
        marginCoin: str,
        startTime: str,
        endTime: str,
        business: str = "",
        pageSize: int = 20,
        lastEndId: str = "",
        next: bool = False,
    ):
        """
        ### Obtain the list of account flow information
        productType: Contract transaction pair productType, ex: "umcbl"
        startTime: Bill start timestamp, ex: "1659403328000"
        endTime: Bill end timestamp, ex: "1659406928000"
        business: Business type, ex: "open_long", "open_short"
        pageSize: Illustrate page size, ex: 20, 50
        lastEndId: Last Id of account bill, ex: "1076451359571689476"
        next: Whether to query the next page, ex: False, True
        """
        params = {}
        if productType and startTime and endTime:
            params["productType"] = productType
            params["marginCoin"] = marginCoin
            params["startTime"] = startTime
            params["endTime"] = endTime
            params["business"] = business
            params["lastEndId"] = lastEndId
            params["pageSize"] = pageSize
            params["next"] = next
            return self._request_with_params(
                GET, MIX_ACCOUNT_V1_URL + "/accountBusinessBill", params
            )
        else:
            return "pls check args"
