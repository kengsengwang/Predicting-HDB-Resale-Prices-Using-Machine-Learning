# scripts/predict_model.py

import pandas as pd
import joblib

def load_model_and_predict(input_dict, model_path="models/best_xgb_model.pkl"):
    # Load model components
    model = joblib.load(model_path)
    scaler = joblib.load("models/scaler.pkl")
    encoder = joblib.load("models/label_encoder.pkl")

    # Convert input to DataFrame
    input_df = pd.DataFrame([input_dict])

    # Scale features
    input_scaled = scaler.transform(input_df)

    # Predict
    y_pred = model.predict(input_scaled)
    y_label = encoder.inverse_transform(y_pred)

    return y_label[0]
