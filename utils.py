def wrap_to_string(df):
    num_cols_list = df["column_name"].to_list()
    num_cols_list = [f'"{i}"' for i in num_cols_list]
    numeric_columns = " ,".join(num_cols_list)
    return numeric_columns