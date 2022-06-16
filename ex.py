import EOD_library
import os
import requests
import json
import numpy as np
import pandas as pd
from typing import Dict
from EOD_library import RequestHandler
API_Token = os.environ.get('API_TOKEN')

# Example
fundamenals = RequestHandler(API_Token)
fundamenal = fundamenals.get_macro_indicators(country='USA')

fundamenal.to_excel('data.xlsx')
print(fundamenal.shape)

# with open('data.json', 'w') as f:
#     json.dump(fundamenal, f)


# f = fundamenal['Financials']['Income_Sntatement']['yearly']

# final_df = pd.DataFrame()
# for x in f:
#     df = pd.DataFrame(data=f[x].values(),
#                       index=f[x].keys())
#     final_df = pd.concat([final_df, df], axis=1)
#     final_df = final_df.rename(columns=df.iloc[0]).drop(df.index[0])

# final_df.to_excel('data.xlsx')
