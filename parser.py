import csv
import pandas as pd

import csv

with open('reddit_wsb.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)
    print(data[0])

# ['timestamp', 'title', 'body', 'score']
data = list(map(lambda x: [x[7], x[0], x[6], x[1]], data))

# filter GME...
GME_data = list(filter(lambda x: "GME" in x[1], data))

# print(GME_data[:10])
