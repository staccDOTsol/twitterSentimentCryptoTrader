DAYS_PER_EPISODE = 25
MINUTES_PER_EPISODE = 24*DAYS_PER_EPISODE*60
NUM_EPISODES = 1
TRADING_FEE_MULTIPLIER = .99925 #this is the trading fee on binance VIP level 0 if using BNB to pay fees
import ccxt
from datetime import datetime
start_time = datetime.utcnow()
print(start_time)
exchange = ccxt.binance({
    'apiKey': '31YHFx31DnLBvNfnohFxhLAnHZtsGrJnkbpbeswutJaetzdflS753Uqnj6pCUB61',
    'secret': '3b9VCQIJlXDGOKEux5odKJMDQhKogsv16KQvd46sk4lTkAaszfftMEwIFraVpY31',
    'timeout': 30000,
    'enableRateLimit': True,
})
ratio = 'BTC'
price = exchange.fetchTicker(ratio + "/USDT")['ask']
print(price)
import random, string
def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))
balances = {}
bal = exchange.fetchBalance()
for b in bal:
    if b == 'total':
        for coin in bal[b]:
            balances[coin] = bal[b][coin]

try:
    #o = exchange.createOrder ('BTC' + '/USDT', 'market', 'buy', balances['USDT'] / price, None, {"newClientOrderId": "x-v0tiKJjj-" + randomword(20)})
    #print(o)
    o = exchange.createOrder ('BTC' + '/USDT', 'market', 'sell', balances['BTC'], None, {"newClientOrderId": "x-v0tiKJjj-" + randomword(20)})
    print(o)
except:
    abc=123
import numpy as np #pip install numpy
from tqdm import tqdm #pip install tqdm
from binance.client import Client #pip install python-binance
import pandas as pd #pip install pandas

import random
from nltk.sentiment.vader import SentimentIntensityAnalyzer 
analyser = SentimentIntensityAnalyzer() 
new_words = {
'bullish': 0.75, 
'bearish': -0.75,
'neutral': 0,
}
analyser.lexicon.update(new_words) 
def sentiment_analyzer_scores(sentence):
    score = analyser.polarity_scores(sentence)
    return(score)
users = ['officialmcafee','vitalikbuterin','satoshilite','pmarca','rogerkver','aantonop', 'ErikVoorhees','nickszabo4','CryptoYoda1338','bgarlinghouse','lopp','barrysilbert','ToneVays','vinnylingham','APompliano','CharlieShrem','gavinandresen','CryptoCobain','winklevoss','MaheshSashital','jimmysong','simoncocking','CryptoHustle','dtapscott','JoelKatz','TimDraper','cryptoSqueeze','laurashin','TheCryptoDog','balajis','CremeDeLaCrypto','iamjosephyoung','Crypto_Bitlord','giacomozucco','woonomic','parabolictrav','el33th4xor','Melt_Dem','haydentiff','CryptoDonAlt','Fisher85M','jonmatonis','stephantual','Beastlyorion','ummjackson','brucefenton','ProfFaustus','dahongfei','kyletorpey','TuurDemeester','TheBlueMatt','slushcz','pierre_rochard','francispouliot_','AriannaSimpson','ArminVanBitcoin','LukeDashjr','justmoon','nathanielpopper','bytemaster7','prestonjbyrne','saifedean','TheCryptoMonk','muneeb','AaronvanW','diiorioanthony','_jonasschnelli_','alansilbert','BitcoinByte','alexsunnarborg','disruptepreneur','chrislarsensf','bitstein','valkenburgh','JedMcCaleb','avsa','nbougalis','adamludwin','oleganza','_jillruth','bendavenport','JackMallers','Xentagz','CryptoTrooper_','ofnumbers','alexbosworth','SDLerner','matthewroszak','CaitlinLong_','TokenHash','Dan_Jeffries1','AlyseKilleen','mikebelshe','DanielKrawisz','conniegallippi','Snyke','minhokim','jamieCrypto','LarryBitcoin','SHodyEsq']

import requests

import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("k7cAVcyoOGsedbSRl5UtoIN6d", "OcbyrBhAYGEWLRanR2U71dLy9RggyXEZIRg1PJ1GDa6wULX0ra")
auth.set_access_token("4352022141-X1y3ZFJ22D8mBe5ELvbOij5OtqVxRVvOlMULwFu", "IU6j4yytn3MVZRwn1F3ChygVPICQ3OHQTa7mMHznZniKU")

# Create API object
api = tweepy.API(auth)
donetweets = []

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
cs = ratios
START_TIME = '24 Jan, 2021'
END_TIME = '21 Feb, 2021'
api_key = "EFnR9fOpJhrNYUYEJZkWu2iLeTFhYZH1fp4aIZgEIl19D9bN1WrsU9vbfIcO0GME"
api_secret = "Jm9G1H9Y2QosonQBaCr67A3LN8Zz88DqWeQOc2Lm6OJOHlDuhRfpQrSdVlYWtMt7"


client = Client(api_key=api_key,api_secret=api_secret)
import time
merge = False
class Memory:
    def __init__(self): 
        self.clear()

    def clear(self): 
        self.actions = []
        
    def add_to_memory(self, new_action): 
        self.actions.append(new_action)
ss = []
tweets2 = {}
import pandas as pd
import numpy as np
import os
#os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64"
#os.environ["PATH"] = os.environ["JAVA_HOME"] + "/bin:" + os.environ["PATH"]
import json
from pyspark.ml import Pipeline
from pyspark.sql import SparkSession
import pyspark.sql.functions as F
from sparknlp.annotator import *
from sparknlp.base import *
import sparknlp
from sparknlp.pretrained import PretrainedPipeline
spark = sparknlp.start()
MODEL_NAME='classifierdl_use_sarcasm'
documentAssembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")
    
use = UniversalSentenceEncoder.pretrained(name="tfhub_use", lang="en")\
 .setInputCols(["document"])\
 .setOutputCol("sentence_embeddings")


sentimentdl = ClassifierDLModel.pretrained(name=MODEL_NAME)\
    .setInputCols(["sentence_embeddings"])\
    .setOutputCol("sentiment")

nlpPipeline = Pipeline(
      stages = [
          documentAssembler,
          use,
          sentimentdl
      ])
## Generating Example Files ##

empty_df = spark.createDataFrame([['']]).toDF("text")
import smtplib
import json
class Env:
    def __init__(self, ratios):
        self.ratios = ratios
        #print(df)
        self.holdings = {}
        self.balance = 1000
        self.net_worth = 0
        #self.main_df = df
        self.reset()
            
    def reset(self):
        self.balances = {'USD':1.0}
        for ratio in self.ratios:
            self.balances[ratio] = 0.0
        #print(len(self.main_df))
        self.iloc = 0#random.randint(0,len(self.main_df)-MINUTES_PER_EPISODE-1)
        #self.episode_df = self.main_df#[self.iloc:self.iloc+24]
        self.money_in = 'USD'
        self.buys = {}
        #self.start_time = self.episode_df['time'].iloc[self.iloc]
        #self.end_time = self.episode_df['time'].iloc[self.iloc-1]
        
    def step(self):
        self.iloc+=1
        #if self.iloc <= MINUTES_PER_EPISODE:
        #print(self.iloc)
        #-------IMPLEMENT STRATEGY HERE--------
        bal = exchange.fetchBalance()
        for b in bal:
            if b == 'total':
                for coin in bal[b]:
                    self.balances[coin] = bal[b][coin]
        for ratio in self.ratios:
            
            #if low sma crosses above high sma
            for s in ss:
                try:
                    if '$' + ratio == s['s'] and ratio != 'USD':
                        #print(ratio)
                        #print(s['score'])
                        if s['score'] > 0.6:
                            
                            #print (s['score'])
                            
                            if start_time < s['dt']:
                                #print(s['dt'])
                                #print(self.episode_df[f'time'][self.iloc])
                                if s['id'] not in donetweets:
                                    donetweets.append(s['id'])
                                    if self.balances[ratio] == 0:
                                #if self.episode_df[f'{ratio}_{SMA_LOW}'][self.iloc] > self.episode_df[f'{ratio}_{SMA_HIGH}'][self.iloc] and self.episode_df[f'{ratio}_{SMA_LOW}'][self.iloc-1] > self.episode_df[f'{ratio}_{SMA_HIGH}'][self.iloc-1]:
                                        self.to_buy = ratio
                                        price = exchange.fetchTicker(ratio + "/USDT")['ask']    
                                        
                                        #buy that ratio (self.to_buy)
                                        
                                        #self.balances[self.to_buy] = (self.balance/3)*TRADING_FEE_MULTIPLIER
                                        #self.holdings[self.to_buy] = (self.balance/3/self.episode_df[f'{self.to_buy}-USD_close'][self.iloc])*TRADING_FEE_MULTIPLIER
                                        tobuyusd = self.balances['USDT'] / 3
                                        tobuy = tobuyusd / price
                                        #self.balance = self.balance - self.balances[self.to_buy]
                                        #print(self.balance)
                                        #self.balances['USD'] = 0.0
                                        self.buy_price = price#self.episode_df[f'{self.to_buy}-USD_close'][self.iloc]
                                        self.buys[self.to_buy] = self.buy_price
                                        print(self.buys)
                                        
                                        print(tweets2[s['id']].created_at)
                                        print(tweets2[s['id']].full_text)
                                        memory.add_to_memory(f'Buy {self.to_buy}: {self.buy_price} datetime: {s["ca"]}')
                                        self.money_in = self.to_buy
                                        #break
                                        try:
                                            exchange.createOrder (ratio + '/USDT', 'market', 'buy', tobuy, None, {"newClientOrderId": "x-v0tiKJjj-" + randomword(20)})
                                        except Exception as e:
                                            print(e)
                                
                except Exception as e:
                    print(e)
        self.balance = self.balances['USDT']
        for s in self.ratios:
            if s != 'USDT' and s in self.buys and self.balances[s] != 0:
                price = exchange.fetchTicker(s + "/USDT")['ask']    
                                        
                if price > 1.15 * self.buys[s] or price < 0.9 * self.buys[s]: 
                #if self.episode_df[f'{self.money_in}_{SMA_LOW}'][self.iloc] < self.episode_df[f'{self.money_in}_{SMA_HIGH}'][self.iloc]:
                    #if high sma crosses below low sma
                    #sell money_in/USD
                    #self.balance += (self.episode_df[f'{s}-USD_close'][self.iloc]*self.holdings[s])*TRADING_FEE_MULTIPLIER
                    #self.balances['USD'] = (self.balances[s]*self.episode_df[f'{s}-USD_close'][self.iloc])*TRADING_FEE_MULTIPLIER
                    #self.balances[s] = 0.0
                    #self.holdings[s] = 0
                    self.sell_price = price
                    memory.add_to_memory(f'Sell {s}: {self.sell_price} datetime: {datetime.utcnow()}' )
                    try:
                        exchange.createOrder (s + '/USDT', 'market', 'sell', self.balances[s], None, {"newClientOrderId": "x-v0tiKJjj-" + randomword(20)})
                    except Exception as e:
                        print(e)
                    #self.money_in = 'USD'
        #-------IMPLEMENT STRATEGY HERE--------
        
        #-------CALCULATE PERFORMANCE METRICS HERE-------
        #Running net worth
        self.net_worth = self.balance
        for ratio in self.ratios: 
            try:
                if self.balances[ratio] > 0:
                    price = exchange.fetchTicker(ratio + "/USDT")['bid']    
                 
                    self.net_worth += self.balances[ratio]*price
            except Exception as e:
                a=1#print(e)
        #Net_worth had you owned all ratios over episode_df --> 'average_market_change'
        """
        self.average_start_price = 0
        self.average_end_price = 0
        for ratio in self.ratios:
            try:
                self.average_start_price += self.episode_df[f'{ratio}-USD_close'].iloc[0]
                self.average_end_price += self.episode_df[f'{ratio}-USD_close'].iloc[-1]
            except:
                abc=123
        self.average_start_price /= len(ratios)
        self.average_end_price /= len(ratios)
        self.average_market_change = self.average_start_price / self.average_end_price
        #-------CALCULATE PERFORMANCE METRICS HERE-------
        """
        return self.net_worth#, self.average_market_change, self.start_time, self.end_time

#select cryptocurrencies you'd like to gather and time interval
merge = False
import os.path
from os import path

env = Env(ratios)
memory = Memory()

net_worth_collect = []
average_market_change_collect = []
from time import sleep
while True:
    lenss = len(ss)
    for u in users:
        try:
            tweets = api.user_timeline(include_rts=False,screen_name=u, count=5, tweet_mode='extended')#u.screen_name, count=10)
            #tweets = [i.AsDict() for i in t]
            for t in tweets:
            
                """
                pipelineModel = nlpPipeline.fit(empty_df)

                df = spark.createDataFrame(pd.DataFrame({"text":[t.full_text]}))
                result = pipelineModel.transform(df)

                #gogo = True
            
                sarcasmis = result.first()['sentiment'][0].__getattr__("result")
                if sarcasmis == 'sarcasm':
                    print(u + ' being sarcastic: ' + t.full_text)
                """
                #print(t.created_at)
                #ts = time.strptime(t.created_at,'%a %b %d %H:%M:%S +0000 %Y')
                dt = t.created_at 
                if dt > datetime.strptime(START_TIME,'%d %b, %Y'):
                    split=(t.full_text).replace('\n', ' ').split(' ')
                    for s in split:
                        #s = s.replace('$','')
                        if s.isupper() or ('$' in s and (s).upper().replace('$','') in cs) and '$' in s:
                            if s in cs or (s).upper().replace('$','') in cs:
                                
                                
                                #print('sentiment score:')
                                #print(sentiment_analyzer_scores(t.full_text)['compound'])
                                if sentiment_analyzer_scores(t.full_text)['compound'] > 0.6:
                                    t.full_text = t.full_text.replace('"', "'")
                                    text_list = []
                                    temp = t.full_text.split(',')
                                    
                                    gogo2 = True
                                    for text in temp:
                                        t2 = text.split('.')
                                        for t3 in t2:
                                        
                                            text_list.append(t3)
                                            #print(t3)
                                            if s in t3 and sentiment_analyzer_scores(t3)['compound'] < 0.2:
                                                gogo2 = False
                                    #print(text_list)
                                    pipelineModel = nlpPipeline.fit(empty_df)

                                    df = spark.createDataFrame(pd.DataFrame({"text":[t.full_text]}))
                                    result = pipelineModel.transform(df)

                                    gogo = True
                                
                                    sarcasmis = result.first()['sentiment'][0].__getattr__("result")
                                    if sarcasmis == 'sarcasm':
                                        gogo = False

                                    if t.created_at > start_time and gogo == True and gogo2 == True:
                                        ss.append({'ca': t.created_at, 'dt': dt, 'id': t.id, 's': s, 'score': sentiment_analyzer_scores(t.full_text)['compound']})
                                        tweets2[t.id] = t
                                        print(t.created_at)
                                        print(ss[-1]['score'])
                                        gmail_user = 'jarettrsdunn@gmail.com'
                                        gmail_password = 'tgfsweltnnnmvryg'
                                        sent_from = gmail_user
                                        to = ['jarettrsdunn@gmail.com', 'carolwerdin@gmail.com']

                                        #to = ['me@gmail.com', 'bill@gmail.com']
                                        subject = u + ' tweeted buy signal about ' + s + '!'
                                        body = u + ' tweeted buy signal about ' + s + '!\n' + t.full_text


                                        email_text = """\
                                        From: %s
                                        To: %s
                                        Subject: %s

                                        %s
                                        """ % (sent_from, ", ".join(to), subject, body)

                                        try:
                                           server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                                           server.ehlo()
                                           server.login(gmail_user, gmail_password)
                                           server.sendmail(sent_from, to, email_text)
                                           server.close()

                                        except:
                                           abc=123#print 'Something went wrong...'
                                        
        except Exception as e:
            a=1#print(e)
    thestep = env.step()
    print('Net worth: $' + str(thestep))
    sleep(60)
    print(memory.actions)