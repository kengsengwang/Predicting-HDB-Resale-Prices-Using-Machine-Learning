import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# === Step 1: Load Dataset ===
def load_data(filepath):
    print(f"📥 Loading data from: {filepath}")
    df = pd.read_csv(filepath)
    print(f"✅ Data loaded. Shape: {df.shape}")
    return df

# === Step 2: Preprocess Dataset ===
def preprocess_data(df):
    # Drop unnecessary or non-numeric columns
    drop_cols = ['block', 'street_name', 'storey_range', 'month']
    df = df.drop(columns=drop_cols, errors='ignore')
    
    # Handle categorical encoding (if needed)
    df = pd.get_dummies(df, drop_first=True)

    # Separate features and target
    X = df.drop(columns=['resale_price'])
    y = df['resale_price']
    
    return train_test_split(X, y, test_size=0.2, random_state=42)

# === Step 3: Train and Evaluate Model ===
def train_model(X_train, y_train):
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    rmse = mean_squared_error(y_test, y_pred, squared=False)
    r2 = r2_score(y_test, y_pred)
    print(f"📊 RMSE: {rmse:.2f}")
    print(f"📈 R² Score: {r2:.4f}")

# === Step 4: Save Model (Optional) ===
def save_model(model, path='resale_model.pkl'):
    joblib.dump(model, path)
    print(f"✅ Model saved to {path}")

# === Main Pipeline ===
if __name__ == "__main__":
    base_dir = r"C:\Users\DELL\Documents\Predicting HDB Resale Prices Using Machine Learning\data"
    file_name = "resale_cleaned.csv"
    file_path = os.path.join(base_dir, file_name)

    df = load_data(file_path)
    X_train, X_test, y_train, y_test = preprocess_data(df)
    model = train_model(X_train, y_train)
    evaluate_model(model, X_test, y_test)
    save_model(model)
