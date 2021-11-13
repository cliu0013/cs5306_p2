import pandas as pd


def getVerdict(pos, neu, neg):
    if pos + neg < neu:
        return 0
    if pos > neg * 1.5:
        return 1
    elif pos <= 1.5 * neg:
        return -1
    else:
        return 0


def getSentiments(stock_name):
    filename = ''
    if stock_name == 's&p':
        filename = 'reddit_wsb_sentiment_counts.csv'
    else:
        filename = 'reddit_wsb_sentiment_counts_gme.csv'
    df = pd.read_csv(filename)
    # convert df to list
    df_list = df.values.tolist()
    dic = {}
    for date, sentiment, count in df_list:
        # convert date to datetime
        date = pd.to_datetime(date)
        if date not in dic:
            dic[date] = {}
        dic[date][sentiment] = count

    # for each date in dic, call get_verdict
    ans = {}
    for date in dic:
        pos = dic[date].get('pos', 0)
        neu = dic[date].get('neu', 0)
        neg = dic[date].get('neg', 0)
        verdict = getVerdict(pos, neu, neg)
        ans[date] = verdict
    return ans

# print(get_sentiments('s&p'))
