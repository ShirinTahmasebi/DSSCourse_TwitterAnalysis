from textblob import TextBlob


def analyze_sentiment(tweet):
    analysis = TextBlob(tweet)
    if analysis.sentiment.polarity > 0:
        return 1
    elif analysis.sentiment.polarity == 0:
        return 0
    else:
        return -1


def get_sentiments_data(tweets):
    processed_tweets_sentiment = []
    for tweet in tweets:
        processed_tweets_sentiment.append(analyze_sentiment(tweet))
    return processed_tweets_sentiment


def get_sentiment_count_summary(tweets):
    pos_tweets = 0
    neu_tweets = 0
    neg_tweets = 0
    for tweet in tweets:
        tweets_sentiment = analyze_sentiment(tweet)
        if tweets_sentiment == 1:
            pos_tweets += 1
        elif tweets_sentiment == 0:
            neu_tweets += 1
        else:
            neg_tweets += 1

    return {
        'Positive': pos_tweets,
        'Neutral': neu_tweets,
        'Negative': neg_tweets,
    }


def get_sentiment_percentage_summary(tweets):
    tweets_sentiment_count = get_sentiment_count_summary(tweets)

    return {
        'Positive': (tweets_sentiment_count['Positive'] * 100) / len(tweets),
        'Neutral': (tweets_sentiment_count['Neutral'] * 100) / len(tweets),
        'Negative': (tweets_sentiment_count['Negative'] * 100) / len(tweets),
    }
