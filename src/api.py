from fastapi import FastAPI
from src.model import load_model, predict

app = FastAPI()
model = load_model()

@app.get("/predict")
def predict_country(country: str):
    if country == "all":
        return {"prediction": "Aggregated results"}
    return {"country": country, "prediction": predict(model, country)}
