import pandas as pd

# with open('reddit_wsb.csv', newline='') as f:
#     reader = csv.reader(f)
#     data = list(reader)
#     print(data[0])

# read data from csv file and convert to list of lists  #
data = pd.read_csv('reddit_wsb.csv')
data = data.values.tolist()

# ['timestamp', 'title', 'body', 'score']
data = list(map(lambda x: [x[7], x[0], x[6], x[1]], data))

# filter GME...
GME_data = list(filter(lambda x: "GME" in x[1], data))

print(GME_data[:10])
