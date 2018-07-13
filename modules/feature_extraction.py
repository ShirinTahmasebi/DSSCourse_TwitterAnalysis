from nltk.corpus import stopwords
import string
from collections import Counter


def get_most_common_words(top_words_number, tweets, key_list=[]):
    punctuation = list(string.punctuation)
    stop = stopwords.words('english') + punctuation + ['rt', 'via']

    count_all = Counter()

    for tweet in tweets:
        word_all = []
        for word in tweet.split(' '):
            if word not in stop:
                word_all.append(word)
        count_all.update(word_all)

    dic = {'most_common': count_all.most_common(top_words_number)}
    for key in key_list:
        dic.update({key: count_all[key]})

    return dic
