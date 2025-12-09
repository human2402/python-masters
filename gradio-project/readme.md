 Gradio-приложение для линейной регрессии

## Запуск через Doker

```bash
docker-compose up --build

```

## Установка и запуск через python

1. Создайте и активируйте виртуальное окружение:

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows
```

2. Установите зависимости:

```bash
pip install -r requirements.txt
```

3. Запуск приложения:

```bash
python app/app.py
```

## Структура проекта

* app/         — код Gradio
* models/      — обученная модель и данные
* requirements.txt
* README.md

## Формат модели

Модель хранится в `models/model.joblib` и загружается с помощью:

joblib.load("models/model.joblib")

## Пример входных данных

x1: 0.5  
x2: 1.2  
x3: -0.3  
x4: 0.9  

## Что показывает приложение

- предсказание модели
- коэффициент R²
- уравнение регрессии в LaTeX
- scatter plot: обучающие данные + выбранная точка