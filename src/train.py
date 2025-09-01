import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
import joblib
import numpy as np
import os

# ---------- 1. Load train/test splits ----------
X_train = pd.read_csv("data/splits/X_train.csv")
X_test = pd.read_csv("data/splits/X_test.csv")
y_train = pd.read_csv("data/splits/y_train.csv")
y_test = pd.read_csv("data/splits/y_test.csv")

# ---------- 2. Initialize and train model ----------
model = LinearRegression()
model.fit(X_train, y_train)

# ---------- 3. Make predictions ----------
y_pred = model.predict(X_test)

# ---------- 4. Evaluate ----------
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)  # manually compute RMSE

print("✅ Model trained successfully!")
print(f"MAE: {mae:.2f}, MSE: {mse:.2f}, RMSE: {rmse:.2f}")

# ---------- 5. Save the model ----------
os.makedirs("models", exist_ok=True)
model_path = "models/linear_regression_model.pkl"
joblib.dump(model, model_path)
print(f"✅ Model saved at {model_path}")
