import os
import requests
import json
import numpy as np
import pandas as pd
API_Token = os.environ.get('API_TOKEN')


class RequestHandler():
    def __init__(self, api_token):
        self.api_token = api_token

    def get_historical_share_price(self, ticker):
        url = 'https://eodhistoricaldata.com/api/eod/{}?fmt=json'.format(
            ticker)
        resp = requests.get(url=url, auth=(
            'api_token', self.api_token))
        df = pd.DataFrame(resp.json())
        df = df.set_index('date')
        return df


price = RequestHandler(API_Token)
print(price.get_historical_share_price(ticker='TSLA.US'))
