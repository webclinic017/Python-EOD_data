import os
import requests
import json
import numpy as np
import pandas as pd
API_Token = os.environ.get('API_TOKEN')


url = (
    'https://eodhistoricaldata.com/api/eod/MCD.US?fmt=json&api_token={}'.format(API_Token))

r = requests.get(url)
data = json.loads(r.text)
df = pd.DataFrame(data)
df = df.set_index('date')
print(df)
