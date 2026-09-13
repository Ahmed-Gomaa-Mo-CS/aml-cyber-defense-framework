import numpy as np

def preprocess(df):
    df = df.copy()
    df = df.select_dtypes(include=[np.number])
    df = df.fillna(0)
    return df
