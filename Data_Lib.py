from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
import sys

import pandas as pd

#API key: U01CH0HHWSRYRL1E
my_key = 'U01CH0HHWSRYRL1E' 
def stockchart(symbol):
    ts = TimeSeries(key=my_key, output_format='pandas')
    data, _meta_data = ts.get_intraday(symbol=symbol,interval='1min', outputsize='full')
    print(data)


    # Graph df as an example
    data['4. close'].plot()
    plt.title('Stock chart')
    plt.show()
    return  data

if __name__ == "__main__":

    symbol=input("Enter symbol name:")
    stockchart(symbol)
    df = stockchart