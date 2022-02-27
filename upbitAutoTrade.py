import time
import pyupbit
from heikinAshi import heikinAshi
from login import login
import datetime
import requests
from slacker import Slacker

print("login start")
upbit = login()
print("login end")
myToken = "xoxb-3187506576960-3149162496183-bW9t043ZmCwwg0jARs2jRZ02"

slack = Slacker(myToken)

def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )

def get_balance(ticker):
    balances = upbit.get_balances()
    for b in balances:
        if b['currency'] == ticker:
            if b['balance'] is not None:
                return float(b['balance'])
            else:
                return 0
    return 0
    
def get_start_time(ticker):
    df = pyupbit.get_ohlcv(ticker, interval="minutes60", count=1)
    start_time = df.index[0]
    return start_time

def get_current_price(ticker):
    return pyupbit.get_orderbook(ticker=ticker)["orderbook_units"][0]["ask_price"]

post_message(myToken,"#upbit", "autotrade start")
flag = 1

while True:
    try:
        now = datetime.datetime.now()
        start_time = get_start_time("KRW-MANA")
        if get_balance("MANA") > 1 :
            flag = 0
        # end_time = start_time + datetime.timedelta(hours=1)
        # if start_time < now < end_time - datetime.timedelta(seconds=10):
        origDf = pyupbit.get_ohlcv("KRW-MANA", interval="minutes60", count = 200)
        heikinAshiDf = heikinAshi(origDf)
        
        # if ((heikinAshiDf['HAclose'][198] > heikinAshiDf['HAopen'][198]) and \
        #     (heikinAshiDf['low'][199] / heikinAshiDf['open'][199] > 0.98)) and flag == 1: 
        if (heikinAshiDf['HAclose'][198] > heikinAshiDf['HAopen'][198]) and flag == 1: 
            flag = 0 
            print('3')
            krw = get_balance("KRW")
            if krw > 50000:
                print('4')
                buy_result = upbit.buy_market_order("KRW-MANA", krw*0.9995)
                print('buy', buy_result)
                post_message(myToken,"#upbit", "MANA buy : " +str(buy_result))
            
        elif (heikinAshiDf['HAclose'][198] < heikinAshiDf['HAopen'][198]) and flag == 0 :
            flag = 1
            print('1')
            coinBalance = get_balance("MANA")
            if coinBalance > 1:                
                print('2')
                sell_result = upbit.sell_market_order("KRW-MANA", coinBalance*0.9995)
                print('sell', sell_result)
                post_message(myToken,"#upbit", "MANA sell : " +str(sell_result))
                
        # elif (heikinAshiDf['low'][199] / heikinAshiDf['open'][199] < 0.98) and flag == 0 : 
        #     flag = 1
        #     coinBalance = get_balance("MANA")
        #     if coinBalance > 1:
        #         sell_result = upbit.sell_market_order("KRW-MANA", coinBalance*0.9995)
        #         print('sell 2', buy_result)
        #         post_message(myToken,"#upbit", "MANA sell : " +str(sell_result))                
        
        print('now :', now ,'price' ,get_current_price("KRW-MANA"),'KRW', get_balance('KRW'), 'MANA', get_balance('MANA'))
        time.sleep(10)
    
    except Exception as e:
        print(e)
        post_message(myToken, "#upbit", e)
        