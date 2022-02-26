import pandas as pd

def heikinAshi(df):
    
    # print(df)
    heikinAshiDf = pd.DataFrame(df, columns=['HAopen', 'high', 'low', 'HAclose', 'open', 'close'])    
    heikinAshiDf['HAclose'] = round((df['open'] + df['high'] + df['low'] + df['close']) / 4, 1)
    
    for i in range(len(df)):
        if i == 0:
            heikinAshiDf.iat[0, 0] = round(df['open'].iloc[0], 1)
            # heikinAshiDf.iat[0, 0] = round((df['HAopen'].iloc[0] + df['HAclose'].iloc[0])/2, 1)
        else:
            heikinAshiDf.iat[i, 0] = round((heikinAshiDf.iat[i-1, 0] + heikinAshiDf.iat[i-1, 3]) / 2, 1)

    heikinAshiDf['high'] = heikinAshiDf.loc[:, ['HAopen', 'HAclose']].join(df['high']).max(axis=1)
    heikinAshiDf['low'] = heikinAshiDf.loc[:, ['HAopen', 'HAclose']].join(df['low']).min(axis=1)
    return heikinAshiDf