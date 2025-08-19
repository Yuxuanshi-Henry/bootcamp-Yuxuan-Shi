def fill_missing_median(df, column_names=None):
    df_copy = df.copy()
    if column_names is None:
        column_names = df_copy.select_dtypes(include=['number']).columns.tolist()
    for col in column_names:
        median_value = df_copy[col].median()
        df_copy[col].fillna(median_value, inplace=True)
    return df_copy


def drop_missing(df, columns=None, threshold=None):
    """ Here threshold between 0 and 1."""
    df_copy = df.copy()
    if columns is not None:
        df_copy.dropna(subset=columns, inplace=True)
        return df_copy
    if threshold is not None:
        df_copy.dropna(thresh=int(threshold*df_copy.shape[1]), inplace=True)
        return df_copy
    return df_copy

def normalize_data(df, columns=None, method='min-max'):
    df_copy = df.copy()
    if columns is None:
        columns = df_copy.select_dtypes(include=['number']).columns.tolist()
    for col in columns:
        if method == 'min-max':
            min_val = df_copy[col].min()
            max_val = df_copy[col].max()
            df_copy[col] = (df_copy[col] - min_val) / (max_val - min_val)
        elif method == 'z-score':
            mean_val = df_copy[col].mean()
            std_val = df_copy[col].std()
            df_copy[col] = (df_copy[col] - mean_val) / std_val

    return df_copy