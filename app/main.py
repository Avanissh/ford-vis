from fastapi import FastAPI
from app.vectorstore import load_index, search, build_and_save
from app.ask import ask_question
from app.recommend import recommend_vehicle
import os

app = FastAPI()

# Auto-build index if not present (handles fresh clone + Docker)
if not os.path.exists("vectorstore/index.faiss"):
    print("🔧 Building FAISS index...")
    build_and_save()
    print("✅ Index ready")
 
index, texts = load_index()


@app.get("/")
def root():
    return {"message": "API is running"}


@app.get("/search")
def search_endpoint(query: str):
    results = search(query, index, texts)
    return {"query": query, "results": results}


@app.get("/ask")
def ask_endpoint(query: str):
    answer = ask_question(query)
    return {"query": query, "answer": answer}


@app.get("/recommend")
def recommend_endpoint(query: str):
    results = recommend_vehicle(query)
    return {"query": query, "recommendations": results}