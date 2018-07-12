from bs4 import BeautifulSoup
import re
import emoji


def handle_text_emojis(tweet):
    # Smile -- :), : ), :-), (:, ( :, (-:, :')
    tweet = re.sub(r'(:\s?\)|:-\)|\(\s?:|\(-:|:\'\))', ' smile ', tweet)
    # Laugh -- :D, : D, :-D, xD, x-D, XD, X-D
    tweet = re.sub(r'(:\s?D|:-D|x-?D|X-?D)', ' laught ', tweet)
    # Love -- <3, :*
    tweet = re.sub(r'(<3|:\*)', ' love ', tweet)
    # Wink -- ;-), ;), ;-D, ;D, (;,  (-;
    tweet = re.sub(r'(;-?\)|;-?D|\(-?;)', ' wink ', tweet)
    # Sad -- :-(, : (, :(, ):, )-:
    tweet = re.sub(r'(:\s?\(|:-\(|\)\s?:|\)-:)', ' sad ', tweet)
    # Cry -- :,(, :'(, :"(
    tweet = re.sub(r'(:,\(|:\'\(|:"\()', ' cry ', tweet)
    return tweet


def handle_iconic_emojis(tweet):
    tweet = emoji.demojize(tweet)
    # Smile
    tweet = re.sub(r'(:smiling_face_with_smiling_eyes:)', ' smile ', tweet)
    tweet = re.sub(r'(:smiling_face_with_sunglasses:)', ' smile ', tweet)
    tweet = re.sub(r'(:smiling_face:)', ' smile ', tweet)
    tweet = re.sub(r'(:slightly_smiling_face:)', ' smile ', tweet)
    tweet = re.sub(r'(:slightly_smiling_face:)', ' smile ', tweet)
    tweet = re.sub(r'(:hugging_face:)', ' smile ', tweet)
    tweet = re.sub(r'(:star-struck:)', ' smile ', tweet)
    # Laugh
    tweet = re.sub(r'(:face_with_tears_of_joy:)', ' laugh ', tweet)
    tweet = re.sub(r'(:grinning_face:)', ' laugh ', tweet)
    tweet = re.sub(r'(:grinning_face_with_big_eyes:)', ' laugh ', tweet)
    tweet = re.sub(r'(:beaming_face_with_smiling_eyes:)', ' laugh ', tweet)
    tweet = re.sub(r'(:rolling_on_the_floor_laughing:)', ' laugh ', tweet)
    tweet = re.sub(r'(:grinning_face_with_smiling_eyes:)', ' laugh ', tweet)
    tweet = re.sub(r'(:grinning_face_with_sweat:)', ' laugh ', tweet)
    tweet = re.sub(r'(:grinning_squinting_face:)', ' laugh ', tweet)
    # Love
    tweet = re.sub(r'(:red_heart:)', ' love ', tweet)
    tweet = re.sub(r'(:kiss_mark:)', ' love ', tweet)
    tweet = re.sub(r'(:smiling_face_with_heart-eyes:)', ' love ', tweet)
    tweet = re.sub(r'(:face_blowing_a_kiss:)', ' love ', tweet)
    # Wink
    tweet = re.sub(r'(:winking_face:)', ' wink ', tweet)
    tweet = re.sub(r'(:winking_face_with_tongue:)', ' wink ', tweet)
    # Sad
    tweet = re.sub(r'(:unamused_face:)', ' sad ', tweet)
    tweet = re.sub(r'(:downcast_face_with_sweat:)', ' sad ', tweet)
    tweet = re.sub(r'(:pensive_face:)', ' sad ', tweet)
    tweet = re.sub(r'(:confused_face:)', ' sad ', tweet)
    tweet = re.sub(r'(:frowning_face:)', ' sad ', tweet)
    tweet = re.sub(r'(:slightly_frowning_face:)', ' sad ', tweet)
    tweet = re.sub(r'(:confounded_face:)', ' sad ', tweet)
    tweet = re.sub(r'(:disappointed_face:)', ' sad ', tweet)
    # Cry
    tweet = re.sub(r'(:sleepy_face:)', ' cry ', tweet)
    tweet = re.sub(r'(:tired_face:)', ' cry ', tweet)
    tweet = re.sub(r'(:crying_face:)', ' cry ', tweet)
    tweet = re.sub(r'(:loudly_crying_face:)', ' cry ', tweet)
    tweet = re.sub(r'(:anxious_face_with_sweat:)', ' cry ', tweet)

    return emoji.emojize(tweet)


def get_cleaned_data(tweets):
    processed_tweets_text = []
    for tweet_id, tweet in enumerate(tweets):
        # HTML decoding
        tweet = BeautifulSoup(tweet, 'lxml').getText()

        # Remove mentions
        tweet = re.sub(r'@[A-Za-z0-9]+', '', tweet)

        # Remove URL links
        tweet = re.sub(r'https?://[A-Za-z0-9./]+', '', tweet)

        # Replace emojies (Iconic or text)
        tweet = handle_text_emojis(tweet)
        tweet = handle_iconic_emojis(tweet)

        # # Remove hashtags, numbers, extra signs and etc
        tweet = re.sub('[^a-zA-Z]', ' ', tweet)

        # Convert more than 2 letter repetitions to 2 letter (funnnnny --> funny)
        tweet = re.sub(r'(.)\1+', r'\1\1', tweet)

        # Convert to lowercase
        tweet = tweet.lower()

        processed_tweets_text.append(tweet)

    return processed_tweets_text
