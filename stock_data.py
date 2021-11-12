import pandas as pd


def get_stock_data(stock_name):

    # read the data from the csv file with stock_name and save to a df variable 
    df = pd.read_csv('{}.csv'.format(stock_name))

    # keep only the date and open price columns
    df = df[['Date','Open']]	


    #sort df by date
    df = df.sort_values(by='Date')

    # change the date column to the datetime format
    df['Date'] = pd.to_datetime(df['Date'])

    # remove dollar sign of the open price column and convert to float, if it is a string
    if(stock_name == 'GME' or stock_name == 'gme'):	
        df['Open'] = df['Open'].str.replace('$','').astype(float)
    return df

get_stock_data('gme')