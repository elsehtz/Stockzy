# graphing visualizers
import matplotlib.pyplot as plt
import matplotlib as pylab
import seaborn

# import local script
import data_retrieval_alpha_vantage as alpha_vantage

class analyzer:

    def __init__(self, stock_name):
        self.selectedStock = str (stock_name)
        return
 
    def get_history(self, how_far_back, time_type="Years", up_to = datetime.date.today()):
    # returns a dataframe
        
        time_type=time_type.lower()
        if(how_far_back==0):
            give_back = (datetime.datetime.today()).replace(ahour=0, minute=0, second=0)
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
if __name__ == "__main__":
    pass