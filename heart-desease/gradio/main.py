import gradio as gr
import joblib
import pandas as pd

SEX_MAP = {"Female": 0, "Male": 1}
CP_MAP = {
    "Typical angina": 1,
    "Atypical angina": 2,
    "Non-anginal pain": 3,
    "Asymptomatic": 4
}
BOOL_MAP = {"No": 0, "Yes": 1}
RESTECG_MAP = {"Normal": 0, "Abnormal": 1, "Hypertrophy": 2}
SLOPE_MAP = {"Up": 0, "Flat": 1, "Down": 2}
THAL_MAP = {"Normal": 3, "Fixed defect": 6, "Reversible defect": 7}



pipe = joblib.load("heart_disease_pipeline.pkl")

def predict(
    age, sex, cp, trestbps, chol, fbs,
    restecg, thalach, exang, oldpeak,
    slope, ca, thal
):
    data = pd.DataFrame([{
        "age": age,
        "sex": sex,              # "male" / "female"
        "cp": cp,                # "angina", "abnang", ...
        "trestbps": trestbps,
        "chol": chol,
        "fbs": fbs,              # "true" / "false"
        "restecg": restecg,      # "norm" / "abn" / "hyper"
        "thalach": thalach,
        "exang": exang,          # "true" / "false"
        "oldpeak": oldpeak,
        "slope": slope,          # "up" / "flat" / "down"
        "ca": ca,
        "thal": thal             # "norm" / "fix" / "rever"
    }])

    proba = pipe.predict_proba(data)[0][1]
    return f"Probability of heart disease: {proba:.2f}"



iface = gr.Interface(
    fn=predict,
    inputs = [
            gr.Number(label="Age"),
            gr.Radio(["Female", "Male"], label="Sex"),
            gr.Dropdown(
                list(CP_MAP.keys()),
                label="Chest pain type"
            ),
            gr.Number(label="Resting blood pressure"),
            gr.Number(label="Cholesterol"),
            gr.Radio(["No", "Yes"], label="Fasting blood sugar > 120"),
            gr.Dropdown(["Normal", "Abnormal", "Hypertrophy"], label="Rest ECG"),
            gr.Number(label="Max heart rate"),
            gr.Radio(["No", "Yes"], label="Exercise induced angina"),
            gr.Number(label="Oldpeak"),
            gr.Dropdown(["Up", "Flat", "Down"], label="Slope"),
            gr.Number(label="Number of vessels"),
            gr.Dropdown(["Normal", "Fixed defect", "Reversible defect"], label="Thal")
        ],

    outputs="text",
    title="Heart Disease Prediction",
)

if __name__ == "__main__":
    iface.launch()
