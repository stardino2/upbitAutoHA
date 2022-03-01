import pyupbit
import hashlib
import os
from urllib.parse import urlencode
from heikinAshi import heikinAshi
from showFigure import showFigure
from login import login
from buySellTest import buySellTest
from buySellTest2 import buySellTest2
import threading
import time
import datetime

res = login()
# print(res.json())

origDf = pyupbit.get_ohlcv("KRW-btc", interval="minutes60", count = 168)
# origDf = pyupbit.get_ohlcv("KRW-bora", interval="day", count = 60)
heikinAshiDf = heikinAshi(origDf)
heikinAshiDf2 = heikinAshi(origDf)

buySellDf = buySellTest(heikinAshiDf, origDf, 'HAclose', 'HAopen')
buySellDf2 = buySellTest2(heikinAshiDf2, origDf, 'HAclose', 'HAopen')
heikinAshiDf['buyPrice'] = buySellDf[0]
heikinAshiDf['sellPrice'] = buySellDf[1]
heikinAshiDf['total'] = buySellDf[2]
heikinAshiDf['direction'] = buySellDf[3]
heikinAshiDf2['buyPrice'] = buySellDf2[0]
heikinAshiDf2['sellPrice'] = buySellDf2[1]
heikinAshiDf2['total'] = buySellDf2[2]
heikinAshiDf2['direction'] = buySellDf2[3]
# heikinAshiDf.to_excel("bora-HAresultM60.xlsx")
# heikinAshiDf2.to_excel("bora-HAresultM60-2.xlsx")

# origDf = pyupbit.get_ohlcv("KRW-bora", interval="minutes240", count = 42)
# heikinAshiDf = heikinAshi(origDf)
# heikinAshiDf2 = heikinAshi(origDf)

# buySellDf = buySellTest(heikinAshiDf, origDf, 'HAclose', 'HAopen')
# buySellDf2 = buySellTest2(heikinAshiDf2, origDf, 'HAclose', 'HAopen')
# heikinAshiDf['buyPrice'] = buySellDf[0]
# heikinAshiDf['sellPrice'] = buySellDf[1]
# heikinAshiDf['total'] = buySellDf[2]
# heikinAshiDf['direction'] = buySellDf[3]
# heikinAshiDf2['buyPrice'] = buySellDf2[0]
# heikinAshiDf2['sellPrice'] = buySellDf2[1]
# heikinAshiDf2['total'] = buySellDf2[2]
# heikinAshiDf2['direction'] = buySellDf2[3]

# def periodiccheck():
#     print('ok')
#     threading.Timer(5, periodiccheck).start()

# periodiccheck()
# print(heikinAshiDf)
# showFigure(heikinAshiDf)
# heikinAshiDf.to_excel("bora-HAresultM240.xlsx")
# heikinAshiDf2.to_excel("bora-HAresultM240-2.xlsx")