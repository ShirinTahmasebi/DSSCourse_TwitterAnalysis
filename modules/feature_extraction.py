from nltk.corpus import stopwords
import string
from collections import Counter


def get_most_common_words(topWordsNumber, tweets):
    punctuation = list(string.punctuation)
    stop = stopwords.words('english') + punctuation + ['rt', 'via']

    count_all = Counter()

    for tweet in tweets:
        word_all = []
        for word in tweet.split(' '):
            if word not in stop:
                word_all.append(word)
        count_all.update(word_all)

    # Print the first 5 most frequent words
    return count_all.most_common(topWordsNumber)


