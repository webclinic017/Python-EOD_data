import os
import requests
import json
import numpy as np
import pandas as pd
from typing import Dict
API_Token = os.environ.get('API_TOKEN')


class RequestHandler():
    def __init__(self, api_token):
        self.api_token = api_token

    def get_historical_share_price(self, ticker: str, params: Dict[str, str] = {}):
        url = 'https://eodhistoricaldata.com/api/eod/{}?fmt=json'.format(
            ticker)
        params['api_token'] = self.api_token
        resp = requests.get(url=url, params=params)
        df = pd.DataFrame(resp.json())
        df = df.set_index('date')
        return df
    # Poosible additional arguments for params:
    # period – use ‘d’ for daily, ‘w’ for weekly, ‘m’ for monthly prices. By default, daily prices will be shown.

    # order – use ‘a’ for ascending dates (from old to new), ‘d’ for descending dates (from new to old). By default, dates are shown in ascending order.

    # from and to – the format is ‘YYYY-MM-DD’. If you need data from Jan 5, 2017, to Feb 10, 2017, you should use from=2017-01-05 and to=2017-02-10.
    # ---------------------------------------------------------------------------

    def get_historical_dividents(self, ticker: str, params: Dict[str, str] = {}):
        url = 'https://eodhistoricaldata.com/api/div/{}?fmt=json'.format(
            ticker)
        params['api_token'] = self.api_token
        resp = requests.get(url=url, params=params)
        df = pd.DataFrame(resp.json())
        df = df.set_index('date')
        return df

    def get_historical_splits(self, ticker: str, params: Dict[str, str] = {}):
        url = 'https://eodhistoricaldata.com/api/splits/{}?'.format(
            ticker)
        params['api_token'] = self.api_token
        resp = requests.get(url=url, params=params)
        return resp.text
    # Poosible additional arguments for params:
    # from – date from with format “Y-m-d”
    # to – date to with format “Y-m-d”
    # ----------------------------------------------------------------------

    def get_options_data(self, ticker: str, params: Dict[str, str] = {}):
        url = 'https://eodhistoricaldata.com/api/options/{}?'.format(
            ticker)
        params['api_token'] = self.api_token
        resp = requests.get(url=url, params=params)
        return resp.json()
    # from - filters OPTIONS by expirationDate. Default value: today.
    # to - filters OPTIONS by expirationDate. Default value: '2100-01-01'
    # trade_date_from - filters OPTIONS by lastTradeDateTime.
    # trade_date_to - filters OPTIONS by lastTradeDateTime.
    # contract_name - returns only the data for particular contract.


# Example
price = RequestHandler(API_Token)
p = price.get_options_data(ticker='AAPL.US', params={'from': '2022-10-10'})
print(p)
