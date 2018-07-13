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
    grouped = remove_rows_with_null_columns(
        data_frame_from_excel,
        filter_column_list=['Country'],
        group_by_column_list=['Country'],
    ).count()
    grouped = prepare_massive_numeric_data_to_view(grouped, 'Country', threshold=0.01)
    plot_bar_x(grouped, 'Country', title='Group By Country', x_label='Countries', y_label='Count')


def second_scenario():
    grouped = remove_rows_with_null_columns(
        data_frame_from_excel,
        filter_column_list=['Date'],
        group_by_column_list=['Date'],
    ).count()

    grouped = prepare_massive_numeric_data_to_view(grouped, 'Date')

    plot_bar_x(grouped, 'Date', title='Group By Date', x_label='Date', y_label='Count')


def third_scenario():
    tweets_with_country_field = remove_rows_with_null_columns(data_frame_from_excel, ['Country'], ['Country'])
    countries = tweets_with_country_field['Country'].values
    for country in set(countries):
        selected_data_frame = data_frame_from_excel.loc[data_frame_from_excel['Country'] == country]

        grouped = remove_rows_with_null_columns(
            selected_data_frame,
            filter_column_list=['Date'],
            group_by_column_list=['Date'],
        ).count()

        grouped = prepare_massive_numeric_data_to_view(grouped, 'Date')

        plot_bar_x(grouped, 'Date', title='Group Tweets From %s By Date' % country, x_label='Date', y_label='Count')


first_scenario()
second_scenario()
third_scenario()
