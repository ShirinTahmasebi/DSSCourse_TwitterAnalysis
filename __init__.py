import pandas as pd
from IPython.display import display
from modules.data_cleaning import get_cleaned_data
from modules.feature_extraction import get_most_common_words
from modules.sentiment_analysis import get_sentiment_percentage_summary
from modules.sql_like_query import *
from modules.visualization import *
import matplotlib.pyplot as plt

file = "apple_dataset.xlsx"

xl = pd.ExcelFile(file)

data_frame_from_excel = xl.parse(xl.sheet_names[0])

cleaned_tweets = get_cleaned_data(data_frame_from_excel['Tweet'])

data_frame_from_excel['Tweet'] = cleaned_tweets

data_frame_from_excel.to_csv('cleaned_dataset.csv')


def first_scenario():
    grouped = filter_group_remove_null_columns(
        data_frame_from_excel,
        filter_column_list=['Country'],
        group_by_column_list=['Country'],
    ).count()
    grouped = prepare_massive_numeric_data_to_view(grouped, 'Country', threshold=0.01)
    plot_bar_x(grouped, 'Country', title='Group By Country', x_label='Countries', y_label='Count')


def second_scenario():
    grouped = filter_group_remove_null_columns(
        data_frame_from_excel,
        filter_column_list=['Date'],
        group_by_column_list=['Date'],
    ).count()

    grouped = prepare_massive_numeric_data_to_view(grouped, 'Date')

    plot_bar_x(grouped, 'Date', title='Group By Date', x_label='Date', y_label='Count')


def third_scenario():
    tweets_with_country_field = filter_group_remove_null_columns(data_frame_from_excel, ['Country'], ['Country'])
    countries = tweets_with_country_field['Country'].values
    for country in set(countries):
        selected_data_frame = data_frame_from_excel.loc[data_frame_from_excel['Country'] == country]

        grouped = filter_group_remove_null_columns(
            selected_data_frame,
            filter_column_list=['Date'],
            group_by_column_list=['Date'],
        ).count()

        grouped = prepare_massive_numeric_data_to_view(grouped, 'Date')

        plot_bar_x(grouped, 'Date', title='Group Tweets From %s By Date' % country, x_label='Date', y_label='Count')


def fourth_scenario():
    sentiments_value = get_sentiment_percentage_summary(cleaned_tweets)
    # sample for sentiment_value = {'Positive': 44.44444444444444, 'Neutral': 44.44444444444444, 'Negative': 11.11111111111111}
    keys = list(sentiments_value.keys())
    values = list(sentiments_value.values())
    data_frame = pd.DataFrame(
        {'Sentiment': keys, 'Values': values}, columns=['Sentiment', 'Values'])
    plot_pie_x(data_frame, keys, 'Values', title='Total Tweets Sentiments')


def fifth_scenario():
    tweets_with_country_field = filter_group_remove_null_columns(data_frame_from_excel, ['Country'], ['Country'])
    countries = tweets_with_country_field['Country'].values
    for country in set(countries):
        selected_data_frame = data_frame_from_excel.loc[data_frame_from_excel['Country'] == country]

        sentiments_value = get_sentiment_percentage_summary(selected_data_frame['Tweet'])
        keys = list(sentiments_value.keys())
        values = list(sentiments_value.values())
        data_frame = pd.DataFrame(
            {'Sentiment': keys, 'Values': values}, columns=['Sentiment', 'Values'])
        plot_pie_x(data_frame, keys, 'Values', title='Group Tweets Sentiments From %s' % country)


def sixth_scenario():
    products_repetition_count = get_most_common_words(
        tweets=cleaned_tweets,
        key_list=['ipod', 'ipad', 'iphone', 'mac', 'ios', 'iwatch'])
    keys = list(products_repetition_count.keys())
    values = list(products_repetition_count.values())
    data_frame = pd.DataFrame(
        {'Products': keys, 'Counts': values}, columns=['Products', 'Counts'])
    plot_pie_x(data_frame, keys, 'Counts', title='Group Tweets By Product')


def seventh_scenario():
    products = ['ipod', 'ipad', 'iphone', 'mac', 'ios', 'iwatch']
    for product in set(products):
        selected_data_frame = data_frame_from_excel.loc[data_frame_from_excel['Tweet'].str.contains(product)]
        if selected_data_frame.values.size == 0:
            continue
        sentiments_value = get_sentiment_percentage_summary(selected_data_frame['Tweet'])
        keys = list(sentiments_value.keys())
        values = list(sentiments_value.values())
        data_frame = pd.DataFrame(
            {'Sentiment': keys, 'Values': values}, columns=['Sentiment', 'Values'])
        plot_pie_x(data_frame, keys, 'Values', title='Group Tweets Sentiments For Product %s' % product)


def eighth_scenario():
    tweets_with_country_field = filter_group_remove_null_columns(data_frame_from_excel, ['Date'], ['Date'])
    dates = tweets_with_country_field['Date'].values
    for date in set(dates):
        selected_data_frame = data_frame_from_excel.loc[data_frame_from_excel['Date'] == date]

        sentiments_value = get_sentiment_percentage_summary(selected_data_frame['Tweet'])
        keys = list(sentiments_value.keys())
        values = list(sentiments_value.values())
        data_frame = pd.DataFrame(
            {'Sentiment': keys, 'Values': values}, columns=['Sentiment', 'Values'])
        plot_pie_x(data_frame, keys, 'Values', title='Group Tweets Sentiments in date %s' % date)


def ninth_scenario():
    tweets_with_date_field = filter_group_remove_null_columns(data_frame_from_excel, ['Date'], ['Date'])
    dates = tweets_with_date_field['Date'].values
    month_date = []
    for date in dates:
        month_date.append(date[0:date.rfind('-')])
    for date in set(month_date):
        selected_data_frame = data_frame_from_excel.loc[data_frame_from_excel['Date'].str.contains(date)]

        sentiments_value = get_sentiment_percentage_summary(selected_data_frame['Tweet'])
        keys = list(sentiments_value.keys())
        values = list(sentiments_value.values())
        data_frame = pd.DataFrame(
            {'Sentiment': keys, 'Values': values}, columns=['Sentiment', 'Values'])
        plot_pie_x(data_frame, keys, 'Values', title='Group Tweets Sentiments in date %s' % date)


first_scenario()
second_scenario()
third_scenario()
fourth_scenario()
fifth_scenario()
sixth_scenario()
seventh_scenario()
eighth_scenario()
ninth_scenario()
