# scripts/train_models.py

import os
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split, GridSearchCV, RandomizedSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import classification_report
from scripts.data_preprocessing import load_and_prepare_data

# === Step 1: Load dataset ===
data_path = r"C:\Users\DELL\Documents\Predicting HDB Resale Prices Using Machine Learning\data\cleaned_resale_transactions.csv"
X, y, le = load_and_prepare_data(data_path)

# === Step 2: Split and scale ===
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# === Step 3: Train Logistic Regression ===
param_grid_lr = {
    'C': [0.1, 1.0, 10.0],
    'solver': ['lbfgs'],
    'multi_class': ['multinomial'],
    'max_iter': [300]
}
grid_lr = GridSearchCV(LogisticRegression(), param_grid_lr, cv=5, scoring='accuracy')
grid_lr.fit(X_train_scaled, y_train)
print("🔹 Logistic Regression:", classification_report(y_test, grid_lr.predict(X_test_scaled)))

# === Step 4: Train Random Forest ===
param_dist_rf = {
    'n_estimators': [100, 200],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5],
    'min_samples_leaf': [1, 2]
}
rand_rf = RandomizedSearchCV(RandomForestClassifier(), param_dist_rf, n_iter=10, cv=5, scoring='accuracy')
rand_rf.fit(X_train, y_train)
print("🌲 Random Forest:", classification_report(y_test, rand_rf.predict(X_test)))

# === Step 5: Train XGBoost ===
param_grid_xgb = {
    'max_depth': [3, 5],
    'n_estimators': [100, 200],
    'learning_rate': [0.01, 0.1]
}
grid_xgb = GridSearchCV(XGBClassifier(objective='multi:softmax', num_class=len(set(y)), eval_metric='mlogloss'),
                        param_grid_xgb, cv=5, scoring='accuracy')
grid_xgb.fit(X_train, y_train)
print("⚡ XGBoost:", classification_report(y_test, grid_xgb.predict(X_test)))

# === Step 6: Save all models and encoders ===
os.makedirs("models", exist_ok=True)
joblib.dump(grid_lr.best_estimator_, "models/best_lr_model.pkl")
joblib.dump(rand_rf.best_estimator_, "models/best_rf_model.pkl")
joblib.dump(grid_xgb.best_estimator_, "models/best_xgb_model.pkl")
joblib.dump(le, "models/label_encoder.pkl")
joblib.dump(scaler, "models/scaler.pkl")

print("✅ All models and encoders saved in /models")
