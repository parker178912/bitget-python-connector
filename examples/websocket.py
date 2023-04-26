#!/usr/bin/python
from bitget_python_connector.consts import CONTRACT_WS_URL
from bitget_python_connector.ws.bitget_ws_client import BitgetWsClient, SubscribeReq


def handle(message):
    print("handle:" + message)


def handel_error(message):
    print("handle_error:" + message)


def handel_btcusd(message):
    print("handel_btcusd:" + message)


if __name__ == '__main__':
    
    api_key = "YOUR_API_KEY"
    secret_key = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    symbol = 'btcusd'

    client = BitgetWsClient(CONTRACT_WS_URL, need_login=True) \
        .api_key(api_key) \
        .api_secret_key(secret_key) \
        .passphrase(passphrase) \
        .error_listener(handel_error) \
        .build()

    channles = [SubscribeReq("mc", "ticker", "BTCUSD"), SubscribeReq("SP", "candle1W", "BTCUSDT")]
    client.subscribe(channles,handle)

    channles = [SubscribeReq("mc", "ticker", "ETHUSD")]
    client.subscribe(channles, handel_btcusd)