# scripts/data_preprocessing.py

import pandas as pd
from sklearn.preprocessing import LabelEncoder

def load_and_prepare_data(filepath, target_col='flat_type'):
    df = pd.read_csv(filepath)

    # Handle 'month' column
    if 'month' in df.columns:
        df['month'] = pd.to_datetime(df['month'], errors='coerce')
        df['year'] = df['month'].dt.year
        df['month_num'] = df['month'].dt.month
        df.drop(columns=['month'], inplace=True)

    # Drop non-numeric columns except target
    y = df[target_col]
    X = df.drop(columns=[target_col])
    X = X.select_dtypes(include=['number'])

    # Encode labels
    le = LabelEncoder()
    y_encoded = le.fit_transform(y)

    return X, y_encoded, le
