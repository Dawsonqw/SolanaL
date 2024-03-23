import tf_python.utils.config_load as config_load
import okx.MarketData as MarketData
import okx.PublicData as PublicData
import json
import datetime

if __name__ == '__main__':
    config=config_load.Config("account_info.json")
    api_key=config.get("api_key")
    secret_key=config.get("secret_key")
    passphrase=config.get("passphrase")
    flag = "1"  # 实盘:0 , 模拟盘：1

    # 获取所有可交易产品的信息列表
    publicDataAPI = PublicData.PublicAPI(flag=flag) 
    # 获取交易产品基础信息
    # instType:
#     SPOT：币币
#     MARGIN：币币杠杆
#     SWAP：永续合约
#     FUTURES：交割合约
#     OPTION：期权
    result = publicDataAPI.get_instruments(
        instType="SWAP"
    )
    print("-------查询可交易产品信息列表----------")
    print("code: ",result["code"])
    print("msg: ",result["msg"])
    
    data=result["data"]
    # for item in data:
    #     print(item["instId"])
    print("-----------------")

        
    # 查询资金费率
    print("-------查询资金费率----------")
    result = publicDataAPI.get_funding_rate(
        instId="BTC-USD-SWAP",
    )
    print("code: ",result["code"])
    print("msg: ",result["msg"])
    data=result["data"]
    for item in data:
        print("资金费率:",item["fundingRate"])
        unix_time=int(item["fundingTime"])
        dt = datetime.datetime.fromtimestamp(unix_time/1000)
        print("资金费率时间:",dt)
        print("下一次资金费率:",item["nextFundingRate"])
        next_unix_time=int(item["nextFundingTime"])
        dt = datetime.datetime.fromtimestamp(next_unix_time/1000)
        print("下一次资金费率时间:",dt)
    print("-----------------")

    
    # 查询限价
    print("-------查询限价----------")
    result = publicDataAPI.get_price_limit(
        instId="BTC-USD-SWAP",
    )
    print("code: ",result["code"])
    print("msg: ",result["msg"])
    data=result["data"]
    for  item in data:
        print("最高买价： ",item["buyLmt"])
        print("最低卖价： ",item["sellLmt"])
        unix_time=int(item["ts"])
        print("更新时间： ",datetime.datetime.fromtimestamp(unix_time/1000))
    print("-----------------")

    
    # 查询标记价格
    print("-------查询标记价格----------")
    result = publicDataAPI.get_mark_price(
        instId="BTC-USD-SWAP",
        instType="SWAP"
    )
    print("code: ",result["code"])
    print("msg: ",result["msg"])
    data=result["data"]
    for item in data:
        print("产品ID： ",item["instId"])
        print("标记价格： ",item["markPx"])
        unix_time=int(item["ts"])
        print("更新时间： ",datetime.datetime.fromtimestamp(unix_time/1000))
    print("-----------------")

    
    # 获取指数行情
    print("-------获取指数行情----------")
    marketDataAPI =  MarketData.MarketAPI(flag=flag)
    result = marketDataAPI.get_index_tickers(
        instId="BTC-USD",
    )
    print("code: ",result["code"])
    print("msg: ",result["msg"])
    data=result["data"]
    for item in data:
        print("产品ID： ",item["instId"])
        print("最新指数价格: ",item["idxPx"])
        print("24h指数最高价： ",item["high24h"])
        print("24h指数最低价： ",item["low24h"])
        print("24h开盘价格： ",item["open24h"])
        print("utc-0开盘价: ",item["sodUtc0"])
        print("utc-8开盘价: ",item["sodUtc8"])
        unix_time=int(item["ts"])
        print("更新时间： ",datetime.datetime.fromtimestamp(unix_time/1000))
    print("-----------------")
    
    
    # 获取指数k线数据 指数K线数据每个粒度最多可获取最近1,440条。
    print("-------获取指数K线数据----------")
    # 获取当前时间之前的4小时对应的时间戳，毫秒级
    now = datetime.datetime.now()
    timestamp = now.timestamp()
    timestamp = int(timestamp*1000)
    start_time = timestamp - 4*60*60*1000

    result = marketDataAPI.get_index_candlesticks(
        instId="BTC-USD",
        before=start_time,
        bar="1H",
        limit="10"
    )
    print("code: ",result["code"])
    print("msg: ",result["msg"])
    data=result["data"]
    for item in data:
        unix_time=int(item[0])
        print("开始时间： ",datetime.datetime.fromtimestamp(unix_time/1000))
        open_price=item[1]
        print("开盘价： ",open_price)
        high_price=item[2]
        print("最高价： ",high_price)
        low_price=item[3]
        print("最低价： ",low_price)
        close_price=item[4]
        print("收盘价： ",close_price)
        confirm=item[5]
        print("k线状态： ",confirm)

        
    # 获取标记价格K线数据
# 标记价格K线数据每个粒度最多可获取最近1,440条。
    print("-------获取标记价格K线数据----------")
    # 获取当前时间之前的4小时对应的时间戳，毫秒级
    now = datetime.datetime.now()
    timestamp = now.timestamp()
    timestamp = int(timestamp*1000)
    start_time = timestamp - 4*60*60*1000

    result = marketDataAPI.get_mark_price_candlesticks(
        instId="BTC-USD-SWAP",
        before=start_time,
        bar="1H",
        limit="10"
    )
    print("code: ",result["code"])
    print("msg: ",result["msg"])
    data=result["data"]
    for item in data:
        unix_time=int(item[0])
        print("开始时间： ",datetime.datetime.fromtimestamp(unix_time/1000))
        open_price=item[1]
        print("开盘价： ",open_price)
        high_price=item[2]
        print("最高价： ",high_price)
        low_price=item[3]
        print("最低价： ",low_price)
        close_price=item[4]
        print("收盘价： ",close_price)
        confirm=item[5]
        print("k线状态： ",confirm)
    print("-----------------")
    