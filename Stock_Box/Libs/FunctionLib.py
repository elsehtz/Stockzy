"""Main Function Library for stock functions"""
#==============================================
###                 IMPORTS                 ###
#==============================================
#Standard libraries
import pandas as pd
import sys
import datetime
import numpy as np
import os

#graphing visualizers
import matplotlib.pyplot as plt
import matplotlib as pylab

#Stock data
import pandas_datareader.data as web
import iexfinance as iex
#from RobinHood import Robinhood
#==============================================
#==============================================

class orginization:

    def __init__(self, *args, **kwargs):
        self.stockDict = {}

    def get_list(self, fileName = "stock_list.txt"):        with open(fileName, 'r') as f:      #ensures file opens properly
            file = f.read()
            self.stockDict = file
        return stocks_arr

    def add_to_list(self, arr, single_stock):
        return arr.append(single_stock)

    def user_search(self):
        pass
    def user_command_stop(self):    
        pass
    def user_command_go(self):
        pass


# dataframe format:
# date / open / high / low / close / volume


class analyzer:

    def __init__(self, stock_name):
        self.selectedStock = str (stock_name)
        return

    def get_history(self, how_far_back, time_type="Years", up_to = datetime.date.today()):
    # returns a dataframe
        
        time_type=time_type.lower()
        if(how_far_back==0):
            give_back = (datetime.datetime.today()).replace(hour=0, minute=0, second=0)
        else:
            if(time_type == "hours"):
                give_back = datetime.datetime.today() - datetime.timedelta(hours=how_far_back)  
            elif(time_type == "days"):
                give_back = datetime.datetime.today() - datetime.timedelta(days=how_far_back)
            else:
                give_back = datetime.datetime.today() - datetime.timedelta(days=(how_far_back*365))
        give_back = give_back.replace(microsecond=0)
        df = iex.get_historical_data(self.selectedStock, start=give_back, end=up_to, output_format='pandas')

        return  df      #  open, high, low, close, volume
    
    def get_price(self):
        stk = iex.Stock(self.selectedStock) 
        stk.get_open()
        print(self.selectedStock)

        return stk.get_price()
    
    def get_past_prices(self):
        ### Fix ###
        stk = iex.Stock(self.selectedStock).chart_table(range="1y")
        
        return stk
    
    def calculate_SMA_15(self, df):
        df["SMA(15)"] = df["close"].rolling(15).mean()
        return df["SMA(15)"]

    def calculate_SMA_30(self, df):
        df["SMA(30)"] = df["close"].rolling(30).mean()
        return df["SMA(30)"]

    def calculate_SMA_100(self, df):
        df["SMA(100)"] = df["close"].rolling(100).mean()
        return df["SMA(100)"]

    def plot_that_shit(self, how_far_back=1, time_type="Years" ):
        ### Needs dates to show on graph and potentaly open windo at set size ###
        df = self.get_history(how_far_back, time_type="Years")
        
        df.append(self.calculate_SMA_100(df))
        df.append(self.calculate_SMA_30(df))
        df.append(self.calculate_SMA_15(df))
        # set colors
        plt.style.use("dark_background")

        df.plot()

        # set Title
        plt.title(self.selectedStock, y=0.9,color='y')
                
        
        #plt.set_facecolor('xkcd:black')
        plt.gca().set_facecolor((0,0,0))

        # graph sizing
        #print(list(df.columns.values))
        lowerBwnd=df['low'].min()-2
        upperBwnd=df['high'].max()+2

        plt.gca().set_ylim([lowerBwnd,upperBwnd])

        # set grid line
        plt.grid(True)

        # show
        plt.draw()
        # at the end call show to ensure window won't close.
        #plt.show()
        
    ###  Move code into sperate py file and run py file from function ###
    def plot_with_seperate_script(self, df):
        df.plot()
        #plt.xticks(df.loc[:,"open"])
        # set colors
        plt.gca().set_facecolor((0,0,0))
        
        # graph sizing
        #print(list(df.columns.values))
        lowerBwnd=df['low'].min()-2
        upperBwnd=df['high'].max()+2
        plt.gca().set_ylim([lowerBwnd,upperBwnd])

        # set grid line
        plt.grid(True)

        plt.draw()
        # at the end call show to ensure window won't close.
        plt.show()
        
        return

    '''
    class trader():
        my_trader = Robinhood()
        def __init__(self, my_trader):
            logged_in = my_trader.login(login_info)
            return         

        def stock_instrument(self, stock):      # I dont like this method; change to using a tuple or dictionary gotten from a file
            return my_trader.instruments(stock)[0]
    
        def quote_info(self, stock):            # primarily for logging
            return my_trader.quote_data(stock)

        def login_info(self):
            return username, password
    
        def store_action():
            pass
    
        def stock_list():
            #stockList[] = 
            return stockList

        def buy():
            pass
    
        def sell():
            pass
     
'''
'''
    from Robinhood import Robinhood
    my_trader = Robinhood()
    logged_in = my_trader.login(username="USERNAME HERE", password="PASSWORD HERE")
    stock_instrument = my_trader.instruments("GEVO")[0]
    quote_info = my_trader.quote_data("GEVO")
    buy_order = my_trader.place_buy_order(stock_instrument, 1)
    sell_order = my_trader.place_sell_order(stock_instrument, 1)
'''
