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
