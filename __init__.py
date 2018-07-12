import pandas as pd
from IPython.display import display
from modules.feature_extraction import get_most_common_words
from modules.data_cleaning import get_cleaned_data
from modules.sentiment_analysis import get_sentiments_data
from modules.sentiment_analysis import get_sentiment_percentage_summary

file = "apple_dataset.xlsx"

xl = pd.ExcelFile(file)

data_frame_from_excel = xl.parse(xl.sheet_names[0])

tweets = data_frame_from_excel['Tweet']

processed_tweets_sentiment = get_sentiments_data(tweets)
processed_tweets_text = get_cleaned_data(tweets)

for i in range(len(tweets)):
    print('Origin: ' + tweets[i])
    print('Cleaned: ' + processed_tweets_text[i])
    print('Sentiment Polarity: %d' % processed_tweets_sentiment[i])

tweets = processed_tweets_text
print(get_sentiment_percentage_summary(tweets))

display(data_frame_from_excel)

data_frame_from_excel.to_csv('cleaned_dataset.csv')

ret = get_most_common_words(25, tweets)
print(ret)
