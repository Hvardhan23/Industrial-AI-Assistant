from pathlib import Path
import joblib

BASE_DIR = Path(__file__).resolve().parents[2]
MODEL_PATH = BASE_DIR / "models" / "xgboost_model.pkl"

print(MODEL_PATH)  # Temporary

model = joblib.load(MODEL_PATH)