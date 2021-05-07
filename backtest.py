1 import pyupbit 
2 import numpy as np 
3 
 
4 # OHLCV(open, high, low, close, volume)로 당일 시가, 고가, 저가, 종가, 거래량에 대한 데이터 
5 df = pyupbit.get_ohlcv("KRW-BTC", count=7) 
6 
 
7 # 변동폭 * k 계산, (고가 - 저가) * k값 
8 df['range'] = (df['high'] - df['low']) * 0.5 
9 
 
10 # target(매수가), range 컬럼을 한칸씩 밑으로 내림(.shift(1)) 
11 df['target'] = df['open'] + df['range'].shift(1) 
12 
 
13 # ror(수익률), np.where(조건문, 참일때 값, 거짓일때 값) 
14 df['ror'] = np.where(df['high'] > df['target'], 
15                      df['close'] / df['target'], 
16                      1) 
17 
 
18 # 누적 곱 계산(cumprod) => 누적 수익률 
19 df['hpr'] = df['ror'].cumprod() 
20 
 
21 # Draw Down 계산 (누적 최대 값과 현재 hpr 차이 / 누적 최대값 * 100) 
22 df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100 
23 
 
24 #MDD 계산 
25 print("MDD(%): ", df['dd'].max()) 
26 
 
27 #엑셀로 출력 
28 df.to_excel("dd.xlsx") 
