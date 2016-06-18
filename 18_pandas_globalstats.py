''' COMPUTING GLOBAL STATISTICS '''

import numpy as np
import pandas as pd
import os

os.chdir("C:\Users\User\Dropbox (Personal)\My Algo Trading Courses\Machine Learning for Trading\ml4t")

def symbol_to_path(symbol, base_dir="data"):
    """Return CSV file path given ticker symbol."""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))


def get_data(symbols, dates):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)
    if 'SPY' not in symbols:  # add SPY for reference, if absent
        symbols.insert(0, 'SPY')

    for symbol in symbols:
        df_temp = pd.read_csv(symbol_to_path(symbol), index_col='Date',
                              parse_dates=True, usecols=['Date','Adj Close'],
                              na_values=['nan'])
        df_temp = df_temp.rename(columns={'Adj Close':symbol})
        if symbol == 'SPY':
            df = df.join(df_temp,how='inner')
            #df = df.join(dt_temp)          # we can also do it this way     
            #df=df.dropna(subset=['SPY'])
        else:
            df = df.join(df_temp,how='left')        
    return df


def test_run():
    
    dates = pd.date_range('2010-01-01','2012-12-31')
    symbols = ['SPY','XOM','GOOG','GLD']
    df = get_data(symbols,dates)
    
if __name__ == "__main__":
    test_run()
