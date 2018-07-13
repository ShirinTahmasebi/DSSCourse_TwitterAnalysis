def remove_rows_with_null_columns(data_frame, filter_column_list=None, result_column_list=None,
                                  group_by_column_list=None):
    if filter_column_list is None:
        filter_column_list = []

    if group_by_column_list is None:
        if result_column_list is None:
            return data_frame.dropna(subset=filter_column_list)
        else:
            return (data_frame.dropna(subset=filter_column_list))[result_column_list]
    else:
        return (data_frame.dropna(subset=filter_column_list)).groupby(group_by_column_list)[group_by_column_list]


def prepare_massive_numeric_data_to_view(data_frame, column_name):
    total = (data_frame.sum()[column_name])
    desired_rows = data_frame[data_frame[column_name] > (total * 0.01)]
    undesired_rows = data_frame[data_frame[column_name] <= (total * 0.01)]
    if undesired_rows.sum()[column_name] > 0:
        desired_rows.loc['Other'] = undesired_rows.sum()[column_name]
    return desired_rows
