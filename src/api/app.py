from fastapi import FastAPI
from src.api.model_loader import model
from src.api.schemas import ChatRequest, MachineInput
from src.feature_engineering.features import engineer_features
import pandas as pd

from src.rag.chatbot import ask_question
from src.rag.rag_pipeline import retriever

app = FastAPI()
from fastapi import HTTPException

#logging, saving data
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("Model Loaded")
logger.info("FAISS Loaded")


@app.post("/predict")
def predict(data: MachineInput):

    df = pd.DataFrame([data.model_dump()])

    df = engineer_features(df)

    prediction = model.predict(df)[0]

    probability = model.predict_proba(df)[0][1]

    return {
        "prediction": int(prediction),
        "failure_probability": round(float(probability),4)
    }

@app.post("/chat")
def chat(request: ChatRequest):

    try:
        answer = ask_question(
            request.question,
            retriever
        )

        return {
            "answer": answer
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

@app.get("/health")
def health():
    return {
        "status": "running",
        "model": "loaded",
        "vector_db": "loaded"
    }

