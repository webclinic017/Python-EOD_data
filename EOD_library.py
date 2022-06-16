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
    code: String. OPTIONAL. To get the data only for Apple Inc (AAPL), use AAPL.US or AAPL ticker code. By default, all possible symbols will be displayed.
    ----------------------------------------------------------------------------"""

    def get_stock_splits_bulk(self, exchange: str, params: Dict[str, str] = {}):
        url = 'https://eodhistoricaldata.com/api/eod-bulk-last-day/{}?fmt=json&type=splits'.format(
            exchange)
        params['api_token'] = self.api_token
        resp = requests.get(url=url, params=params)
        df = pd.DataFrame(resp.json())
        df = df.set_index('code')
        return df

    def get_stock_dividends_bulk(self, exchange: str, params: Dict[str, str] = {}):
        url = 'https://eodhistoricaldata.com/api/eod-bulk-last-day/{}?fmt=json&type=dividends'.format(
            exchange)
        params['api_token'] = self.api_token
        resp = requests.get(url=url, params=params)
        df = pd.DataFrame(resp.json())
        df = df.set_index('code')
        return df
    """Additional arguments for params:
    date - format : 2022-03-03"""

    def get_list_of_tickers(self, exchange: str, params: Dict[str, str] = {}):
        url = 'https://eodhistoricaldata.com/api/exchange-symbol-list/{}?fmt=json&type=dividends'.format(
            exchange)
        params['api_token'] = self.api_token
        resp = requests.get(url=url, params=params)
        df = pd.DataFrame(resp.json())
        df = df.set_index('Code')
        return df
    """------------------------------------------------------------------"""

    def get_macro_indicators(self, country: str, params: Dict[str, str] = {}):
        url = 'https://eodhistoricaldata.com/api/macro-indicator/{}?fmt=json'.format(
            country)
        params['api_token'] = self.api_token
        resp = requests.get(url=url, params=params)
        df = pd.DataFrame(resp.json())
        df = df.set_index('CountryCode')
        return df
    """
    COUNTRY: String. REQUIRED. Defines the country for which the indicator will be shown. The country should be defined in the Alpha-3 ISO format. Possible values: USA, FRA, DEU
    
    Additional arguments for params:
    indicator: String. OPTIONAL. Defines which macroeconomics data indicator will be shown. See the list of possible indicators below. The default value is ‘gdp_current_usd‘.
    
    List of Available Macroeconomics Indicators

    ‘real_interest_rate‘ – Real interest rate (%).
    ‘population_total‘ – Population, total.
    ‘population_growth_annual‘ – Population growth (annual %).
    ‘inflation_consumer_prices_annual‘ – Inflation, consumer prices (annual %).
    ‘consumer_price_index‘ – Consumer Price Index (2010 = 100).
    ‘gdp_current_usd‘ – GDP (current US$).
    ‘gdp_per_capita_usd‘ – GDP per capita (current US$).
    ‘gdp_growth_annual‘ – GDP growth (annual %).
    ‘debt_percent_gdp‘ – Debt in percent of GDP (annual %).
    ‘net_trades_goods_services‘ – Net trades in goods and services (current US$).
    ‘inflation_gdp_deflator_annual‘ – Inflation, GDP deflator (annual %).
    ‘agriculture_value_added_percent_gdp‘ – Agriculture, value added (% of GDP).
    ‘industry_value_added_percent_gdp‘ – Industry, value added (% of GDP).
    ‘services_value_added_percent_gdp‘ – Services, etc., value added (% of GDP).
    ‘exports_of_goods_services_percent_gdp‘ – Exports of goods and services (% of GDP).
    ‘imports_of_goods_services_percent_gdp‘ – Imports of goods and services (% of GDP).
    ‘gross_capital_formation_percent_gdp‘ – Gross capital formation (% of GDP).
    ‘net_migration‘ – Net migration (absolute value).
    ‘gni_usd‘ – GNI, Atlas method (current US$).
    ‘gni_per_capita_usd‘ – GNI per capita, Atlas method (current US$).
    ‘gni_ppp_usd‘ – GNI, PPP (current international $).
    ‘gni_per_capita_ppp_usd‘ – GNI per capita, PPP (current international $).
    ‘income_share_lowest_twenty‘ – Income share held by lowest 20% (in %).
    ‘life_expectancy‘ – Life expectancy at birth, total (years).
    ‘fertility_rate‘ – Fertility rate, total (births per woman).
    ‘prevalence_hiv_total‘ – Prevalence of HIV, total (% of population ages 15-49).
    ‘co2_emissions_tons_per_capita‘ – CO2 emissions (metric tons per capita).
    ‘surface_area_km‘ – Surface area (sq. km).
    ‘poverty_poverty_lines_percent_population‘ – Poverty headcount ratio at national poverty lines (% of population).
    ‘revenue_excluding_grants_percent_gdp‘ – Revenue, excluding grants (% of GDP).
    ‘cash_surplus_deficit_percent_gdp‘ – Cash surplus/deficit (% of GDP).
    ‘startup_procedures_register‘ – Start-up procedures to register a business (number).
    ‘market_cap_domestic_companies_percent_gdp‘ – Market capitalization of listed domestic companies (% of GDP).
    ‘mobile_subscriptions_per_hundred‘ – Mobile cellular subscriptions (per 100 people).
    ‘internet_users_per_hundred‘ – Internet users (per 100 people).
    ‘high_technology_exports_percent_total‘ – High-technology exports (% of manufactured exports).
    ‘merchandise_trade_percent_gdp‘ – Merchandise trade (% of GDP).
    ‘total_debt_service_percent_gni‘ – Total debt service (% of GNI).
    ---------------------------------------------------------------------------------"""

    def get_fundamentals(self, ticker: str, params: Dict[str, str] = {}):
        url = 'https://eodhistoricaldata.com/api/fundamentals/{}?'.format(
            ticker)
        params['api_token'] = self.api_token
        resp = requests.get(url=url, params=params)
        return resp.json()
    """----------------------------------------------------------------"""
