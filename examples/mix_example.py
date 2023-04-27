import bitget_python_connector.mix.market_api as market
import bitget_python_connector.mix.account_api as accounts
import bitget_python_connector.mix.position_api as position
import bitget_python_connector.mix.order_api as order
import bitget_python_connector.mix.plan_api as plan
import bitget_python_connector.mix.trace_api as trace
from bitget_python_connector.client import Client

## MIX 合約
if __name__ == '__main__':

    api_key = "YOUR_API_KEY"
    secret_key = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"

    client = Client(api_key, secret_key, passphrase)
    symbol = 'BTCUSDT_UMCBL'

## 1. Market API 公共行情街口
    market_config = market.MarketApi(client.API_KEY, client.API_SECRET_KEY, client.PASSPHRASE)

    # Get contract list 合约信息接口
    market_config.contracts('umcbl')

    # Get depth data 深度行情接口
    market_config.depth(symbol, limit=100)

    # Get ticker information according to the currency pair 单个Ticker行情获取
    market_config.ticker(symbol)

    # Get all ticket information 全部Ticker行情获取
    market_config.tickers('dmcbl')

    # Get real-time transaction 获取最近成交明细
    market_config.fills(symbol, limit=50)

    # Obtain K line information 获取K线数据
    market_config.candles(symbol, granularity='1m',startTime=1679103025000, endTime=1679104945000,limit=100)

    # Currency index price 获取K线数据
    market_config.index(symbol)

    # Next settlement time 获取合约下一次结算时间
    market_config.funding_time(symbol)

    # Contract Mark Price 获取合约标记价格
    market_config.market_price(symbol)

    # Historical fund rate 获取历史资金费率
    market_config.history_fund_rate(symbol,pageSize=20,pageNo=1, nextPage=False)

    # Current fund rate 获取当前资金费率
    market_config.current_fund_rate(symbol)

    # Obtain the total position of the platform 获取平台总持仓量
    market_config.open_interest(symbol)

## 2. Account API 帳戶接口
    account_config = accounts.AccountApi(api_key, secret_key, passphrase, use_server_time=False, first=False)

    # Obtain user account information 单个币种账户信息
    account_config.account(symbol, marginCoin='USDT')

    # Adjusting lever 调整杠杆
    account_config.leverage(symbol, marginCoin='USDT', leverage=20, holdSide='long')

    # Adjustment margin 调整保证金
    account_config.margin(symbol, marginCoin='USDT', amount=20, holdSide='long')

    # Adjust margin mode 调节保证金模式
    account_config.margin_mode(symbol, marginCoin='USDT', marginMode='crossed')
    
    # Set position mode 调节单双向持仓模式
    account_config.position_mode(symbol, marginCoin='USDT', holdMode='double_hold')

    # Query the number of open sheets 获取可开数量
    account_config.open_count(symbol, marginCoin='USDT', openPrice='3000', openAmount='500', leverage=20)

    # Get account information list 获取账户信息列表
    account_config.accounts('umcbl')

## 3. 倉位接口
    positionApi = position.PositionApi(api_key, secret_key, passphrase, use_server_time=False, first=False)

    # Obtain the user's single position information 获取单个合约仓位信息
    positionApi.single_position(symbol, marginCoin='USDT')
    
    # Obtain all position information of the user 获取全部合约仓位信息
    positionApi.all_position(productType='mix_type')

## 4. 交易接口
    order_config = order.OrderApi(api_key, secret_key, passphrase, use_server_time=False, first=False)
    
    # Place an order 下单
    order_config.place_order(symbol="TRXUSDT_UMCBL", marginCoin='USDT', size=555,side='open_long', orderType='limit', price='0.0333', timeInForceValue='normal')

    # Place orders in batches 批量下单
    order_data=[{"price":"0.0333","size":"666","side":"open_long","orderType":"limit","timeInForceValue":"normal",}]
    order_config.batch_orders("TRXUSDT_UMCBL", marginCoin='USDT', order_data=order_data)

    # Cancel the order 撤单
    order_config.cancel_orders(symbol, marginCoin='USDT', orderId='804554549183000576')

    # Batch cancellation 批量撤单
    order_config.cancel_batch_orders(symbol, marginCoin='USDT', orderIds=['804557496038076416','804557496121962497'])

    # Get order information 获取订单详情
    order_config.detail(symbol, orderId='804557496038076416')

    # Get the current order 获取当前委托
    order_config.current(symbol)

    # Get Historical Delegation 获取历史委托
    order_config.history(symbol, startTime='1627454102000', endTime='1627547623000', pageSize=20, lastEndId='',isPre=False)

    # Obtain transaction details 查询成交明细
    order_config.fills(symbol, orderId='804553570245029890')

## 5. 计划委托接口
    plan_config = plan.PlanApi(api_key, secret_key, passphrase, use_server_time=False, first=False)

    # Plan Entrusted Order 计划委托下单
    plan_config.place_plan(symbol, marginCoin='USDT', size='1', side='open_long', orderType='limit', triggerPrice='39782', executePrice='38982', triggerType='fill_price', timeInForceValue='normal')
    
    # Modify Plan Delegation 修改计划委托
    plan_config.modify_plan(symbol, marginCoin='USDT', orderId='804602672390836225', orderType='limit', triggerPrice='39782', executePrice='37222', triggerType='fill_price')

    # Modify the preset profit and loss stop of plan entrustment 修改计划委托预设止盈止损
    plan_config.modify_plan_preset(symbol, marginCoin='USDT', orderId='804602672390836225', planType='normal_plan', presetTakeProfitPrice='45000', presetStopLossPrice='34678')

    # Modify the preset profit and loss stop of plan entrustment 修改止盈止损
    plan_config.modify_tpsl_plan(symbol, marginCoin='USDT', orderId='804602672390836225', planType='normal_plan', triggerPrice='45000')
    
    # Stop profit and stop loss Order 止盈止损下单
    plan_config.place_tpsl(symbol, marginCoin='USDT', planType='normal_plan', triggerPrice='45000', holdSide='open_long')

    # Planned entrustment (profit and loss stop) cancellation 计划委托(止盈止损)撤单
    plan_config.cancel_plan(symbol, marginCoin='USDT', orderId='804600814695845888', planType='normal_plan')

    # Get the current plan delegation 获取当前计划委托(止盈止损)列表
    plan_config.current_plan(symbol, isPlan='plan')

    # Get historical plan delegation 获取历史计划委托(止盈止损)列表
    plan_config.history_plan(symbol, startTime='1627454102000', endTime='1627558127000', pageSize=20, lastEndId='', isPlan='plan')

## 6. 跟單委托接口
    trace_config = trace.TraceApi(api_key, secret_key, passphrase, use_server_time=False, first=False)

    # Followers obtain information on opening and closing orders 跟随者获取历史跟单信息
    trace_config.follower_history_orders('10', '1', '1635782400000', '1635852263953')

    # Details of traders to be distributed 交易员待分润明细
    trace_config.wait_profit_detail("10","1")

    # Get trader copytrader symbol 获取交易员跟单交易对
    trace_config.trader_symbols()

    # Set trader copytrader symbol 交易员设置跟单交易对
    trace_config.set_trder_symbol("BTCUSDT_UMCBL")