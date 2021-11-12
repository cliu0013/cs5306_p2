import operator
from nltk import sentiment
import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer
import numpy as np

# # import nltk
# # nltk.download('vader_lexicon')

# # with open('reddit_wsb.csv', newline='') as f:
# #     reader = csv.reader(f)
# #     data = list(reader)
# #     print(data[0])

# # read data from csv file and convert to list of lists  #
# df = pd.read_csv('reddit_wsb.csv')

# df = df[df['title'].str.contains('gme') == False]
# df = df[df['title'].str.contains('GME') == False]

# # data = data.values.tolist()

# # ['timestamp', 'title', 'body', 'score']
# # data = list(map(lambda x: [x[7], x[0], x[6], x[1]], data))

# # print(df['title'])

# sia = SentimentIntensityAnalyzer()
# df["sentiment_score"] = df["title"].apply(
#     lambda x: sia.polarity_scores(x)["compound"])
# df["sentiment"] = np.select([df["sentiment_score"] < 0, df["sentiment_score"] == 0, df["sentiment_score"] > 0],
#                             ['neg', 'neu', 'pos'])

# # count the number of positive, negative, and neutral comments #
# df["sentiment"].value_counts()

# # print(df["sentiment"])

# # make the timpstamp only date #
# df["timestamp"] = pd.to_datetime(df["timestamp"])
# df["date"] = df["timestamp"].dt.date

# #for each date, count the number positive, negative, and neutral comments #
# sentiments = df.groupby("date")["sentiment"].value_counts()


def getSentiments(stock):
    keep = False if stock == "s&p" else True

    df = pd.read_csv('reddit_wsb.csv')

    df = df[df['title'].str.contains('gme') == keep]
    df = df[df['title'].str.contains('GME') == keep]

    # data = data.values.tolist()

    # ['timestamp', 'title', 'body', 'score']
    # data = list(map(lambda x: [x[7], x[0], x[6], x[1]], data))

    # print(df['title'])

    sia = SentimentIntensityAnalyzer()
    df["sentiment_score"] = df["title"].apply(
        lambda x: sia.polarity_scores(x)["compound"])
    df["sentiment"] = np.select([df["sentiment_score"] < 0, df["sentiment_score"] == 0, df["sentiment_score"] > 0],
                                ['neg', 'neu', 'pos'])

    # count the number of positive, negative, and neutral comments #
    df["sentiment"].value_counts()

    # print(df["sentiment"])

    # make the timpstamp only date #
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df["date"] = df["timestamp"].dt.date

    #for each date, count the number positive, negative, and neutral comments #
    sentiments = df.groupby("date")["sentiment"].value_counts()
    return sentiments.to_frame()
