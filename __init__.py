import pandas as pd
from IPython.display import display
from modules.data_cleaning import get_cleaned_data
from modules.feature_extraction import get_most_common_words
from modules.sentiment_analysis import get_sentiment_percentage_summary
from modules.sql_like_query import *
from modules.visualization import *

file = "apple_dataset.xlsx"

xl = pd.ExcelFile(file)

data_frame_from_excel = xl.parse(xl.sheet_names[0])

tweets = data_frame_from_excel['Tweet']

display(data_frame_from_excel)

tweets = get_cleaned_data(tweets)
print(get_sentiment_percentage_summary(tweets))

data_frame_from_excel.to_csv('cleaned_dataset.csv')

ret = get_most_common_words(25, tweets)
print(ret)

ret = get_most_common_words(2, tweets,
                            ['apple', 'Apple', 'iPod', 'ipod', 'iPad', 'ipad', 'iPhone', 'iphone', 'mac', 'Mac', 'IOS',
                             'ios', 'iWatch', 'iwatch', 'Watch', 'watch'])
print(ret)

tweets = data_frame_from_excel.dropna(subset=['Country'])
print(tweets['Country'])

print(remove_rows_with_null_columns(data_frame_from_excel, ['Country']))

#### First Scenario ####
grouped = remove_rows_with_null_columns(
    data_frame_from_excel,
    filter_column_list=['Country'],
    group_by_column_list=['Country'],
).count()

grouped = prepare_massive_numeric_data_to_view(grouped, 'Country')

plot_bar_x(grouped, title='Group By Country', x_label='Countries', y_label='Count')
