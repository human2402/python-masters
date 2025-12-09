import joblib
import json
from pathlib import Path
import numpy as np


BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "model.joblib"
INFO_PATH = BASE_DIR / "models" / "model_info.json"


def load_model():
    """
    Загружает модель линейной регрессии из joblib.
    """
    return joblib.load(MODEL_PATH)


def load_model_info():
    """
    Загружает коэффициенты + R2, сохранённые заранее.
    """
    with open(INFO_PATH, "r", encoding="utf-8") as f:
        return json.load(f)
