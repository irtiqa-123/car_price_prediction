import os

# Use your existing project folder
project_root = "."  # current directory is already car_price_prediction

# Folders to create inside existing project
folders = [
    "data",   # CSV dataset
    "models", # trained model
    "src"     # Python scripts
]

# Files to create inside src/
src_files = [
    "data_ingest.py",
    "preprocess.py",
    "train.py",
    "evaluate.py",
    "app.py"
]

# ---------- Create folders ----------
for folder in folders:
    path = os.path.join(project_root, folder)
    os.makedirs(path, exist_ok=True)
    print(f"Folder ready: {path}")

# ---------- Create empty script files in src/ ----------
src_path = os.path.join(project_root, "src")
os.makedirs(src_path, exist_ok=True)

for file in src_files:
    file_path = os.path.join(src_path, file)
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            pass
        print(f"File created: {file_path}")
    else:
        print(f"File already exists: {file_path}")

print("\n✅ Only `data/`, `models/`, `src/` and scripts inside `src/` are created in your existing project!")
