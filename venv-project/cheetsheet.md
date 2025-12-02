
## 1. Создание окружения
```
python -m venv .venv
```

## 2. Активация
```
.venv\Scripts\Activate.ps1
```
## 3. Описание зависимостей

### `requirements_ML.txt`

```
numpy
pandas
scikit-learn
seaborn
plotly
```

### `requirements_service.txt`

```
fastapi
uvicorn[standard]
gradio
```

### `requirements_jupyter.txt`

```
jupyter
ipython
```

---

### `.gitignore`

```
.venv/
__pycache__/
.ipynb_checkpoints/
```


## 4. Установка зависимостей

### ML пакеты:

```bash
pip install -r requirements_ML.txt
```

### Сервисные пакеты:

```bash
pip install -r requirements_service.txt
```

### Jupyter:

```bash
pip install -r requirements_jupyter.txt
```

---
![](.\screenshoots\null.png)

## 5. Запуск uvicorn

```bash
uvicorn app.main:app --reload
```

------


![](.\screenshoots\image.png)


























