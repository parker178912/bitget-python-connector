import bitget_python_connector.spot.public_api as public
import bitget_python_connector.spot.market_api as market
import bitget_python_connector.spot.account_api as account
import bitget_python_connector.spot.order_api as order
import bitget_python_connector.spot.plan_api as plan
from bitget_python_connector.client import Client

## SPOT 現貨
if __name__ == '__main__':

    api_key = "YOUR_API_KEY"
    secret_key = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"

    client = Client(api_key, secret_key, passphrase)
    symbol = 'BTCUSDT_SPBL'

    ## 1. Public API 基礎配置街口
    public_config = public.PublicApi(client.API_KEY, client.API_SECRET_KEY, client.PASSPHRASE)

    # Obtain server time 获取服务器时间
    public_config.times()

    # Obtain all coins information on the platform 币种基础信息
    public_config.currencies()

    # Obtain basic configuration information of all trading pairs 获取所有币对基础配置信息
    public_config.products()

    # Obtain all ticker information 获取单个产品信息
    public_config.product(symbol)

    ## Market API 公共行情街口
    market_config = market.MarketApi(client.API_KEY, client.API_SECRET_KEY, client.PASSPHRASE);
    
    # Get Single Ticker 获取某个Ticker信息
    market_config.ticker(symbol)

    # Get All Tickers 获取全部Ticker信息
    market_config.tickers()
    
    # Get Recent Trades 获取最近成交数据
    market_config.fills(symbol, limit=50)

    # Get depth 获取深度数据
    market_config.depth(symbol, limit=50, type='step0')

    # Get Candle Data 获取K线数据
    market_config.candles(symbol, period='1min', after='1624352586', before='1624356186', limit=100)

    ## 2. Account API 帳戶接口
    account_config = account.AccountApi(client.API_KEY, client.API_SECRET_KEY, client.PASSPHRASE)

    # Obtain account assets 获取账户资产
    account_config.assets()

    # Obtain transaction detail flow 获取账单流水
    account_config.bills()

    ## 3. Order API 訂單接口
    order_config = order.OrderApi(client.API_KEY, client.API_SECRET_KEY, client.PASSPHRASE)

    # Place order 下单
    order_config.orders(symbol, price='2.30222', quantity='1', side='buy', orderType='limit', force='normal', clientOrderId='spot#29028939ss')

    # Batch order 批量下单
    order_data=[{"price":"2.30222","quantity":"1","side":"buy","orderType":"limit","force":"normal","client_oid":"spot#jidhuu19399"}, {"price":"2.30111","quantity":"1","side":"buy","orderType":"limit","force":"normal","client_oid":"spot#akncnai8821"}]
    order_config.batch_orders(symbol, order_data=order_data)
    
    # Cancel order 撤单
    order_config.cancel_orders(symbol, orderId='791171749756964864')

    # Cancel batch orders 批量撤单
    order_config.cancel_batch_orders(symbol, orderId=[''])

    # Get order List 获取未成交列表
    order_config.open_order(symbol)

    # Get order history 获取历史委托列表
    order_config.history(symbol)

    # Get transaction details 获取成交的历史明细
    order_config.fills(symbol)

    ## 4. Plan API 计划委托接口
    plan_config = plan.PlanApi(api_key, secret_key, passphrase, use_server_time=False, first=False)

    # Place plan order 下计划委托
    result = plan_config.placePlan(symbol, side='buy', triggerPrice='22031', executePrice='22031', size='50', triggerType='market_price', orderType='market', timeInForceValue='normal')

    # Modify plan order 修改计划委托
    plan_config.modifyPlan(orderId='987136018723487744', triggerPrice='22031', executePrice='22031', size='50', orderType='market')

    # Cancel plan order 撤销计划委托
    plan_config.cancelPlan(orderId='987136018723487744')

    # Get current plan orders 获取当前计划委托
    plan_config.currentPlan(symbol, pageSize='5')
    
    # Get history plan orders 获取历史计划委托
    plan_config.historyPlan(symbol, pageSize='5', startTime='1671005531000', endTime='1671085652000')