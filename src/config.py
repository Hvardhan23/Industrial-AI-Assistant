from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

MODEL_PATH = BASE_DIR / "models/xgboost_model.pkl"

PDF_PATH = BASE_DIR / "data/docs/Maintenance_Manual.pdf"

VECTOR_DB = BASE_DIR / "data/vector_db"