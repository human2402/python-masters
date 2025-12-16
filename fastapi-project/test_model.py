import pytest
from app.model import load_model, predict_value
from app.config import settings


TEST_INPUT = [0, 2, 0, 0]
EXPECTED_OUTPUT = 129.170

def test_load_model():
    """Модель должна успешно загружаться"""
    model = load_model()
    assert model is not None

def test_predict_value_type():
    """Предсказание должно быть числом (float)"""
    model = load_model()
    pred = predict_value(model, TEST_INPUT)
    assert isinstance(pred, float)

def test_predict_known_value():
    """Предсказание для известного входа совпадает с ожидаемым"""
    model = load_model()
    pred = predict_value(model, TEST_INPUT)
    # Используем округление, чтобы избежать мелких погрешностей
    assert round(pred, 2) == round(EXPECTED_OUTPUT, 2)

