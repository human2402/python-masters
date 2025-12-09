# API для линейной регрессии

## Endpoints

* v1/ping
* v1/predict (body example: {"x": [0,1,0,0]})
* v1/model_info

## Структура

app/ — код API  
models/ — модель + инфо  
.env — параметры  
docker-compose.yml — запуск через Docker  

## Тест модели

```bash
pytest tests/test_model.py
```

## Запуск докер контейнера

```bash
docker-compose up --build
```

## Запуск локально

```bash
uvicorn app.main:app --reload
