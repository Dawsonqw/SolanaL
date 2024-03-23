import tf_python.utils.config_load as config_load
import tf_python.utils.message as message
import okx.MarketData as MarketData
import okx.PublicData as PublicData
import json
import logging
import time
import datetime


if __name__ == '__main__':
    config=config_load.Config("account_info.json")
    api_key=config.get("api_key")
    secret_key=config.get("secret_key")
    passphrase=config.get("passphrase")
    webhook=config.get("webhook")
    flag = "1"  # 实盘:0 , 模拟盘：1
    DingdingSender=message.DingDingMessage(webhook,"remote")
    marketDataAPI =  MarketData.MarketAPI(flag=flag)

    # 存储5s前的价格
    pre_price=0
    while True:
        now = datetime.datetime.now()
        timestamp = now.timestamp()
        timestamp = int(timestamp*1000)
        start_time = timestamp - 2*60*1*1000

        result = marketDataAPI.get_index_tickers(
            instId="BTC-USD",
            quoteCcy="USDT"
        )
        data=result["data"]
        for item in data:
            unix_time=int(item["ts"])
            cur_price=float(item["idxPx"])
            if pre_price == 0:
                pre_price=cur_price
                continue
            else:
                change_rate=(cur_price-pre_price)/pre_price
                pre_price=cur_price
                # 如果绝对值大于0.5，发送消息提醒
                if abs(change_rate)>0.5:
                    message="当前价格:"+str(cur_price)+"\n涨跌幅:"+str(change_rate)
                    DingdingSender.send(message)
        time.sleep(5)