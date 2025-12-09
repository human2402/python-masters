import numpy as np
import pandas as pd
import joblib
import gradio as gr # type: ignore
import matplotlib.pyplot as plt


def make_plot(best_feature, X_train, y_train, user_value, user_prediction):
    """Строит scatter: обучающие точки + точка пользователя"""

    fig, ax = plt.subplots(figsize=(6, 4))

    # Точки train
    ax.scatter(
        X_train[best_feature],
        y_train,
        alpha=0.6,
        label="train data"
    )

    # Точка пользователя
    ax.scatter(
        [user_value],
        [user_prediction],
        s=100,
        label="user input",
        edgecolor="black"
    )

    ax.set_xlabel(best_feature)
    ax.set_ylabel("target")
    ax.legend()
    return fig


def predict(*inputs):
    """
    inputs — 4 или больше признаков, введённых пользователем.
    Функция возвращает:
    - предсказание,
    - график,
    - LaTeX формулу регрессии.
    """

    X = pd.DataFrame([inputs], columns=feature_names)

    y_pred = model.predict(X)[0]

    fig = make_plot(
        best_feature,
        train,
        target.values.ravel(),
        X[best_feature].iloc[0],
        y_pred
    )

    latex_eq = r"$$y = " + " + ".join(
        [f"{coef[i]:.2f} \cdot x_{i}" for i in range(len(coef))]
    ) + f" + {model.intercept_:.2f}$$"

    return y_pred, fig, latex_eq


model = joblib.load("models/model.joblib")

train = pd.read_csv("data/train.csv")      # X_train с колонками признаков
target = pd.read_csv("data/train_y.csv")   # y_train

# выбираем признак с наибольшим по абсолютной величине коэффициентом
feature_names = train.columns.tolist()

coef = model.coef_
best_feature = feature_names[np.argmax(np.abs(coef))]
print("Лучший признак -", best_feature)


# web интерфейс с Gradio
inputs = [
    gr.Number(label=name) for name in feature_names
]

# Выходные данные
outputs = [
    gr.Number(label="Predicted y"),
    gr.Plot(label="Scatter Plot"),
    gr.Markdown(label="Regression Equation (LaTeX)")
]

# R2 в description
r2_text = f"R² модели: {model.score(train, target):.3f}"

app = gr.Interface(
    fn=predict,
    inputs=inputs,
    outputs=outputs,
    title="Линейная регрессия",
    description=r2_text,
    article="Введите значения признаков — получите предсказание."
)

app.launch(server_name="0.0.0.0", server_port=7860)
