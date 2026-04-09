import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import os

model = SentenceTransformer("all-MiniLM-L6-v2")


# Load all text data
def load_texts():
    texts = []

    for file in ["data/vehicles.json", "data/service.json", "data/manuals.json"]:
        with open(file) as f:
            data = json.load(f)
            for item in data:
                texts.append(item["text"])

    return texts


# Create embeddings
def create_embeddings(texts):
    return model.encode(texts).astype("float32")


# Build + save FAISS index
def build_and_save():
    texts = load_texts()
    embeddings = create_embeddings(texts)

    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)

    os.makedirs("vectorstore", exist_ok=True)
    faiss.write_index(index, "vectorstore/index.faiss")

    with open("vectorstore/texts.json", "w") as f:
        json.dump(texts, f)

    print("✅ Index built and saved")


# Load index
def load_index():
    index = faiss.read_index("vectorstore/index.faiss")

    with open("vectorstore/texts.json") as f:
        texts = json.load(f)

    return index, texts


# Intent extraction (clean logic)
def extract_intent(query):
    query = query.lower()

    if "family" in query or "7 seat" in query:
        return {"type": "SUV", "seats": 7}

    if "pickup" in query or "towing" in query:
        return {"type": "Pickup"}

    if "sport" in query or "performance" in query:
        return {"type": "Coupe"}

    return {}


# Search with hybrid filtering
def search(query, index, texts, k=5):
    query_vec = model.encode([query]).astype("float32")
    distances, indices = index.search(query_vec, k)

    intent = extract_intent(query)
    results = []

    for i in indices[0]:
        text = texts[i]

        if intent:
            if "type" in intent and intent["type"] not in text:
                continue
            if "seats" in intent and str(intent["seats"]) not in text:
                continue

        results.append(text)

    return results[:3]