import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import os

# ---------- 1. Load dataset ----------
df = pd.read_csv("data/vehicle_data.csv")

# ---------- 2. Encode categorical features ----------
categorical_cols = ["brand", "fuel_type"]
encoder = OneHotEncoder(sparse_output=False)  # fixed for scikit-learn 1.2+
encoded = encoder.fit_transform(df[categorical_cols])
encoded_df = pd.DataFrame(encoded, columns=encoder.get_feature_names_out(categorical_cols))

# ---------- 3. Combine with numerical features ----------
numerical_cols = ["year", "mileage"]
X = pd.concat([df[numerical_cols], encoded_df], axis=1)
y = df["price"]

# ---------- 4. Split into train/test ----------
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ---------- 5. Save the splits ----------
os.makedirs("data/splits", exist_ok=True)
X_train.to_csv("data/splits/X_train.csv", index=False)
X_test.to_csv("data/splits/X_test.csv", index=False)
y_train.to_csv("data/splits/y_train.csv", index=False)
y_test.to_csv("data/splits/y_test.csv", index=False)

print("✅ Preprocessing complete. Train/test splits saved in data/splits/")
