import operator
import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer
import numpy as np

# import nltk
# nltk.download('vader_lexicon')

# with open('reddit_wsb.csv', newline='') as f:
#     reader = csv.reader(f)
#     data = list(reader)
#     print(data[0])

# read data from csv file and convert to list of lists  #
df = pd.read_csv('reddit_wsb.csv')

df = df[df['title'].str.contains('gme') == False]
df = df[df['title'].str.contains('GME') == False]

# data = data.values.tolist()

# ['timestamp', 'title', 'body', 'score']
# data = list(map(lambda x: [x[7], x[0], x[6], x[1]], data))

print(df['title'])

sia = SentimentIntensityAnalyzer()
df["sentiment_score"] = df["title"].apply(
    lambda x: sia.polarity_scores(x)["compound"])
df["sentiment"] = np.select([df["sentiment_score"] < 0, df["sentiment_score"] == 0, df["sentiment_score"] > 0],
                            ['neg', 'neu', 'pos'])

print(df["sentiment"])

# filter GME...
# GME_data = list(filter(lambda x: "GME" in x[1], data))

# print(GME_data[:10])


# import csv
# import pandas as pd


# with open('reddit_wsb.csv', newline='') as f:
#     reader = csv.reader(f)
#     data = list(reader)
#     # print(data[0])

# # ['timestamp', 'title', 'body', 'score']
# data = list(map(lambda x: [x[7], x[0], x[6], x[1]], data))

# # filter GME...
# GME_data = list(filter(lambda x: "GME" in x[1], data))

# print(GME_data[:10])
