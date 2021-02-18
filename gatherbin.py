import numpy as np #pip install numpy
from tqdm import tqdm #pip install tqdm
from binance.client import Client #pip install python-binance
import pandas as pd #pip install pandas
from datetime import datetime
import random

SMA_LOW = 40
SMA_HIGH = 150

def compute_sma(data, window):
    sma = data.rolling(window=window).mean()
    return sma

import requests
r = requests.get("https://api.binance.com/api/v3/ticker/24hr").json()
symbols = []
for sym in r:
    if 'BTC' in sym['symbol']:
        if sym['symbol'].replace('BTC','') not in symbols:
            symbols.append(sym['symbol'].replace('BTC',''))
#select cryptocurrencies you'd like to gather and time interval
ratios = symbols
START_TIME = '1 Jan, 2021'
END_TIME = '18 Feb, 2021'
api_key = "EFnR9fOpJhrNYUYEJZkWu2iLeTFhYZH1fp4aIZgEIl19D9bN1WrsU9vbfIcO0GME"
api_secret = "Jm9G1H9Y2QosonQBaCr67A3LN8Zz88DqWeQOc2Lm6OJOHlDuhRfpQrSdVlYWtMt7"


client = Client(api_key=api_key,api_secret=api_secret)
import time
merge = False
bads = []
for ratio in ratios:
    try:
        print(f'Gathering {ratio} data...')
        data = client.get_historical_klines(symbol=f'{ratio}USDT',interval=Client.KLINE_INTERVAL_1HOUR,start_str=START_TIME,end_str=END_TIME)
        cols = ['time','Open','High','Low',f'{ratio}-USD_close',f'{ratio}-USD_volume','CloseTime','QuoteAssetVolume','NumberOfTrades','TBBAV','TBQAV','null']
        
        temp_df = pd.DataFrame(data,columns=cols)
        temp_df = temp_df[['time',f'{ratio}-USD_close']]
        for col in temp_df.columns:
            if col != 'time':
                temp_df[col] = temp_df[col].astype(np.float64)
        for i in tqdm(range(len(temp_df))):
            try:
                temp_df['time'][i] = datetime.fromtimestamp(int(temp_df['time'][i]/1000))
            except Exception as e:
                print(e)
                abc=123
        if merge == False:
            df = temp_df
            df.to_csv(ratio)
        else:
            df = pd.merge(df,temp_df,how='inner',on='time')
        merge = False
        print('complete')
    except Exception as e:
        bads.append(ratio)
    time.sleep(10) #sleep for a bit so the binance api doesn't kick you out for too many data asks




#clip NaNs

#convert binance timestamp to datetime

df.to_csv('12-coins-Mar18_Jun20')
