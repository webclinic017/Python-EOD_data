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
    """Additional arguments for params:
    period – use ‘d’ for daily, ‘w’ for weekly, ‘m’ for monthly prices. By default, daily prices will be shown.

    order – use ‘a’ for ascending dates (from old to new), ‘d’ for descending dates (from new to old). By default, dates are shown in ascending order.

    from and to – the format is ‘YYYY-MM-DD’. If you need data from Jan 5, 2017, to Feb 10, 2017, you should use from=2017-01-05 and to=2017-02-10.
    ---------------------------------------------------------------------------"""

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
    """Additional arguments for params:
    from – date from with format “Y-m-d”
    to – date to with format “Y-m-d”
    ----------------------------------------------------------------------"""

    def get_options_data(self, ticker: str, params: Dict[str, str] = {}):
        url = 'https://eodhistoricaldata.com/api/options/{}?'.format(
            ticker)
        params['api_token'] = self.api_token
        resp = requests.get(url=url, params=params)
        return resp.json()
    """Additional arguments for params:
    from - filters OPTIONS by expirationDate. Default value: today.
    to - filters OPTIONS by expirationDate. Default value: '2100-01-01'
    trade_date_from - filters OPTIONS by lastTradeDateTime.
    trade_date_to - filters OPTIONS by lastTradeDateTime.
    contract_name - returns only the data for particular contract.
    ---------------------------------------------------------"""

    def get_historical_market_cap(self, ticker: str, params: Dict[str, str] = {}):
        url = 'https://eodhistoricaldata.com/api/historical-market-cap/{}?'.format(
            ticker)
        params['api_token'] = self.api_token
        resp = requests.get(url=url, params=params)
        df = pd.DataFrame(resp.json())
        df = df.transpose()
        df = df.set_index('date')
        return df
    """Additional arguments for params:
    from and to – the format is ‘YYYY-MM-DD’. If you need data from Jan 5, 2017, to Feb 10, 2017, you should use from=2017-01-05 and to=2017-02-10."""

    def get_insider_transactions(self, ticker: str, params: Dict[str, str] = {}):
        url = 'https://eodhistoricaldata.com/api/insider-transactions?{}'.format(
            ticker)
        params['api_token'] = self.api_token
        resp = requests.get(url=url, params=params)
        df = pd.DataFrame(resp.json())
        df = df.set_index('date')
        return df
    """Additional arguments for params:
    limit: Number. OPTIONAL. The limit for entries per result, from 1 to 1000. Default value: 100.
    from and to: String. OPTIONAL. The format is ‘YYYY-MM-DD’. If you need data from Jan 1, 2021, to Feb 10, 2021, you should use from=2021-01-15 and to=2021-02-10. Default value: to – the current date, from – one year ago.
    code: String. OPTIONAL. To get the data only for Apple Inc (AAPL), use AAPL.US or AAPL ticker code. By default, all possible symbols will be displayed."""

    def get_fundamentals(self, ticker: str, params: Dict[str, str] = {}):
        url = 'https://eodhistoricaldata.com/api/fundamentals/{}?'.format(
            ticker)
        params['api_token'] = self.api_token
        resp = requests.get(url=url, params=params)
        return resp.json()
    """--------------------------------------------------------------------"""


# Example
fundamenals = RequestHandler(API_Token)
fundamenal = fundamenals.get_fundamentals(ticker='IPR.LS')


# with open('data.json', 'w') as f:
#     json.dump(fundamenal['Financials']['Income_Statement']['yearly'], f)


# f = fundamenal['Financials']['Income_Statement']['yearly']

# final_df = pd.DataFrame()
# for x in f:
#     df = pd.DataFrame(data=f[x].values(),
#                       index=f[x].keys())
#     final_df = pd.concat([final_df, df], axis=1)
#     final_df = final_df.rename(columns=df.iloc[0]).drop(df.index[0])

# final_df.to_excel('data.xlsx')
