import pandas as pd

stock_name = 's&p'

# read the data from the csv file with stock_name and save to a df variable 
df = pd.read_csv('{}.csv'.format(stock_name))

# keep only the date and open price columns
df = df[['Date','Open']]	


#sort df by date
df = df.sort_values(by='Date')

# change the date column to the datetime format
df['Date'] = pd.to_datetime(df['Date'])

print(df.head())