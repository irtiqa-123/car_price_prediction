import pandas as pd
import os

# ---------- 1. Ensure data folder exists ----------
os.makedirs("data", exist_ok=True)

# ---------- 2. Load vehicle dataset ----------
csv_path = "data/vehicle_data.csv"  # fixed path

try:
    df = pd.read_csv(csv_path)
    print("✅ Data loaded successfully!")
except FileNotFoundError:
    print(f"❌ File not found: {csv_path}")
    exit()

# ---------- 3. Quick data preview ----------
print("\n--- First 5 rows ---")
print(df.head())

print("\n--- Dataset Info ---")
print(df.info())

print("\n--- Basic Statistics ---")
print(df.describe())
