from fastapi import APIRouter                                   #type: ignore
from pydantic import BaseModel                                 #type: ignore                                
from app.model import load_model, predict_value, model_info       

router = APIRouter(prefix="/v1")

class PredictRequest(BaseModel):
    x: list[float]

@router.get("/ping")
def ping():
    return {"status": "ok"}

@router.post("/prediction")
def predict(req: PredictRequest):
    model = load_model()
    pred = predict_value(model, req.x)
    return {"prediction": pred}

@router.get("/model_info")
def info():
    return model_info()
