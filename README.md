Industrial AI Assistant for Predictive Maintenance
Project Overview

This project combines machine learning and Generative AI to help with industrial machine maintenance. The application predicts whether a machine is likely to fail based on its operating conditions and also answers maintenance-related questions using information from a maintenance manual.

The prediction model is built using XGBoost, while the chatbot uses Retrieval-Augmented Generation (RAG) with FAISS, Hugging Face embeddings, LangChain, and Google's Gemini model. Both features are exposed through FastAPI APIs and the entire application is containerized using Docker.

Features
Predict machine failure using an XGBoost model.
Generate additional features such as temperature difference and power.
Answer maintenance-related questions from a PDF manual using RAG.
REST APIs built with FastAPI.
Docker support for easy deployment.
Tech Stack

Programming Language

Python

Machine Learning

XGBoost
Scikit-learn
Pandas
NumPy

RAG

LangChain
FAISS
Hugging Face Embeddings
Google Gemini

Backend

FastAPI
Uvicorn

Deployment

Docker
Project Workflow
Dataset
   │
   ▼
Data Preprocessing
   │
   ▼
Feature Engineering
   │
   ▼
XGBoost Model
   │
   ▼
FastAPI
   │
   ├──────────────► /predict
   │
   └──────────────► /chat
                      │
                  FAISS Retriever
                      │
                  Gemini
                      │
                  Final Response
API Endpoints
POST /predict

Predicts whether a machine is likely to fail.

Example Request

{
  "Type": 0,
  "Air_temperature_K": 298.1,
  "Process_temperature_K": 308.6,
  "Rotational_speed_rpm": 1551,
  "Torque_Nm": 42.8,
  "Tool_wear_min": 0
}
POST /chat

Answers questions using the maintenance manual.

Example Request

{
  "question": "How do I inspect bearings?"
}
GET /health

Checks whether the API, prediction model, and vector database are loaded successfully.

Future Improvements
Save and load the FAISS index instead of rebuilding it at startup.
Add automated tests.
Deploy the application on Google Cloud or AWS.
Improve logging and configuration management.