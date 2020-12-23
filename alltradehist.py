#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 20:15:25 2018

@author: ayx
"""
# reference: http://cryptocurrenciesstocks.readthedocs.io/kraken.html#ohlc

import ccs
import ast

response = ccs.kraken.public.getOHLCdata("ETHUSD", interval=30, since=1000)
a=ast.literal_eval(response)['result']
df=pd.DataFrame(a[list(a.keys())[0]])
date_str(df.iloc[0,0])
df.columns=['time','open','high','low','close','vwap','volume','count']
df.sort_values(by=['time'], ascending=True, inplace=True)

date_str(1438956205.7754)