import json
import joblib
from app.config import settings

def load_model():
    """Загружает модель из файла"""
    return joblib.load(settings.MODEL_PATH)

def predict_value(model, x):
    """Возвращает предсказание"""
    return float(model.predict([x])[0])

def model_info():
    """Возвращает коэффициенты и R2"""
    with open(settings.MODEL_INFO_PATH, "r") as f:
        return json.load(f)
