import pandas as pd
import joblib
import numpy as np
import os
from sklearn.metrics import mean_absolute_error, mean_squared_error

# ---------- 1. Load test data ----------
X_test = pd.read_csv("data/splits/X_test.csv")
y_test = pd.read_csv("data/splits/y_test.csv")

# ---------- 2. Load trained model ----------
model_path = "models/linear_regression_model.pkl"
model = joblib.load(model_path)
print(f"✅ Model loaded from {model_path}")

# ---------- 3. Make predictions ----------
y_pred = model.predict(X_test)

# ---------- 4. Calculate metrics ----------
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

print("✅ Evaluation complete")
print(f"MAE: {mae:.2f}, MSE: {mse:.2f}, RMSE: {rmse:.2f}")

# ---------- 5. Save metrics ----------
os.makedirs("metrics", exist_ok=True)
metrics_df = pd.DataFrame({
    "MAE": [mae],
    "MSE": [mse],
    "RMSE": [rmse]
})
metrics_df.to_csv("metrics/evaluation_metrics.csv", index=False)
print("✅ Metrics saved at metrics/evaluation_metrics.csv")
