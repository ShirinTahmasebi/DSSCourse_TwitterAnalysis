import pandas as pd
from nltk.corpus import stopwords
import string
from collections import Counter


file = "../sentiment/apple_dataset.xlsx"

xl = pd.ExcelFile(file)

data_frame_from_excel = xl.parse(xl.sheet_names[0])

tweets = data_frame_from_excel['Tweet']

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
print(count_all.most_common(25))

