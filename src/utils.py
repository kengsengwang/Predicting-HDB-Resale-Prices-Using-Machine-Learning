# src/utils.py

import joblib
import os
import pandas as pd
from sklearn.preprocessing import LabelEncoder

def save_model(model, filepath="model.joblib"):
    joblib.dump(model, filepath)
    print(f"✅ Model saved to {filepath}")

def load_model(filepath="model.joblib"):
    if os.path.exists(filepath):
        model = joblib.load(filepath)
        print(f"✅ Model loaded from {filepath}")
        return model
    else:
        print("❌ Model file not found!")
        return None

def encode_categorical(df, categorical_cols):
    """
    Encodes categorical columns using LabelEncoder.
    Returns transformed dataframe and dictionary of encoders.
    """
    encoders = {}
    for col in categorical_cols:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col].astype(str))
        encoders[col] = le
    return df, encoders
