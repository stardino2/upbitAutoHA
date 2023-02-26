import pyupbit
import numpy as np

#get_ohlcv 함수는 고가/시가/저가/종가/거래량을 DataFrame으로 반환합니다.
df = pyupbit.get_ohlcv("KRW-BTC", count = 120)

df['range'] = (df['high'] - df['low']) * 0.2
df['target'] = df['open'] + df['range'].shift(1)

fee = 0.0005
df['ror'] = np.where(df['high'] > df['target'],
                     df['close'] / df['target'] - fee,
                     1)

df['hpr'] = df['ror'].cumprod()
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100
print("MDD(%): ", df['dd'].max())
print(df)
print(df['hpr'].max())
# df.to_excel("dd.xlsx")
