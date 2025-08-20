import numpy as np
from datetime import datetime
import datetime as dt
import pandas as pd
from typing import List, Dict


def calc_mean_std(lst):
    '''calculate mean and std of a list of numbers'''
    arr = np.array(lst)
    return arr.mean(), arr.std()


def log_call(func):
    '''A decorator that logs the function call with timestamp'''
    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} called at {dt.datetime.now()}")
        return func(*args, **kwargs)
    return wrapper


@log_call 
def calc_mean_std_logged(lst):
    '''A logged version of calc_mean_std'''
    return calc_mean_std(lst)


def safe_stamp():
    '''generate a safe timestamp string'''
    return dt.datetime.now().strftime("%Y%m%d-%H%M%S")


def safe_filename(prefix: str, meta: Dict[str, str]) -> str:
    '''generate a safe filename with prefix, metadata, and timestamp'''
    mid = "_".join([f"{k}-{str(v).replace(' ', '-')[:20]}" for k, v in meta.items()])
    return f"{prefix}_{mid}_{safe_stamp()}.csv"


def validate_df(df: pd.DataFrame, required_cols: List[str], dtypes_map: Dict[str, str]) -> Dict[str, str]:
    '''validate a DataFrame for required columns and data types'''
    msgs = {}
    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        msgs['missing_cols'] = f"Missing columns: {missing}"
    for col, dtype in dtypes_map.items():
        if col in df.columns:
            try:
                if dtype == 'datetime64[ns]':
                    pd.to_datetime(df[col])
                elif dtype == 'float':
                    pd.to_numeric(df[col])
            except Exception as e:
                msgs[f'dtype_{col}'] = f"Failed to coerce {col} to {dtype}: {e}"
    na_counts = df.isna().sum().sum()
    msgs['na_total'] = f"Total NA values: {na_counts}"
    return msgs


def fill_missing_median(df, column_names=None):
    '''Fill missing values in specified columns with their median values'''
    df_copy = df.copy()
    if column_names is None:
        column_names = df_copy.select_dtypes(include=['number']).columns.tolist()
    for col in column_names:
        median_value = df_copy[col].median()
        df_copy[col].fillna(median_value, inplace=True)
    return df_copy


def drop_missing(df, columns=None, threshold=None):
    """ drop rows with missing values in specified columns or based on a threshold. 
    Here threshold between 0 and 1."""
    df_copy = df.copy()
    if columns is not None:
        df_copy.dropna(subset=columns, inplace=True)
        return df_copy
    if threshold is not None:
        df_copy.dropna(thresh=int(threshold*df_copy.shape[1]), inplace=True)
        return df_copy
    return df_copy


def normalize_data(df, columns=None, method='min-max'):
    '''Normalize specified columns in a DataFrame using min-max or z-score normalization'''
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