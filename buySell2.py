import numpy as np

def buySell2(df, origDf, closePrice, openPrice):
    sigPriceBuy = [] 
    sigPriceSell = []
    total = []
    currentDirection = ''
    direction = []
    money = 100
    flag = 1
    res = 0
    for i in range(0, len(df)): 
        if (df[closePrice][i-1] > df[openPrice][i-1]) and flag == 1: 
        # (df[closePrice][i-2] < df[openPrice][i-2]) and \        
            sigPriceBuy.append(origDf['open'][i]) 
            sigPriceSell.append(np.nan) 
            flag = 0 
            money = money * 0.9995 / origDf['open'][i]
            total.append(np.nan)
            
        elif (df[closePrice][i-1] < df[openPrice][i-1]) and flag == 0 : 
        # (df[closePrice][i-2] > df[openPrice][i-2]) and \        
            sigPriceSell.append(origDf['open'][i]) 
            sigPriceBuy.append(np.nan) 
            flag = 1
            money = money * origDf['open'][i] * 0.9995
            total.append(money)
            res = money
            
        else: 
            sigPriceSell.append(np.nan) 
            sigPriceBuy.append(np.nan)
            total.append(np.nan)
        
        if (df[closePrice][i] < df[openPrice][i]) :
            currentDirection = '-'
            direction.append(currentDirection)
            
        elif (df[closePrice][i] > df[openPrice][i]) :
            currentDirection = '+'
            direction.append(currentDirection)
            
        else :
            direction.append(currentDirection)            
            
    print('2 : ' , res)
    return (sigPriceBuy, sigPriceSell, total, direction)