
## Установка UV
```
pip install uv
```

## Создание виртуального окружения
```
uv venv .venv
```

## Активация
```
.venv\Scripts\Activate.ps1      # Windows PowerShell
source .venv/bin/activate       # Linux
```
## Инициализация UV проекта
```
uv init
```
## Добавление зависимостей
```
uv add fastapi
```

## Запуск FastApi
uv умеет сам запускать ASGI-приложения через встроенный сервер
```
uv run app.main:app
```
но он **не отслеживает изменения** по этому
```
uv run uvicorn app.main:app --reload
```
![](src\screen.png)
