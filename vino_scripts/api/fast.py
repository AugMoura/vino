from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
#from vino_scripts.interface.main import pred
#from vino_scripts.ml_logic.registry import load_model
import pandas as pd

app = FastAPI()
#app.state.model = load_model() # Preferably model should be loaded before invoking prediction

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


@app.get("/predict")
def predict():      # Insert fields required for prediction
    """
    Predicts y based on X inputs from frontend
    """
    X_pred = pd.DataFrame(dict()) # Dict to receive fields from the function

    predict = pred(X_pred)

    return {"fare_amount": float(predict)}


@app.get("/")
def root():
    return {"greeting": "Hello"}
