import json
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# 1. Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

# 2. Load data
def load_texts():
    texts = []

    for file in ["data/vehicles.json", "data/service.json", "data/manuals.json"]:
        with open(file) as f:
            data = json.load(f)
            for item in data:
                texts.append(item["text"])

    return texts

# 3. Create embeddings
def create_embeddings(texts):
    return model.encode(texts).astype("float32")

# 4. Build FAISS index
def build_index(embeddings):
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)
    return index

# 5. Search
def search(query, index, texts):
    query_vec = model.encode([query]).astype("float32")
    distances, indices = index.search(query_vec, 3)

    return [texts[i] for i in indices[0]]


# 🚀 RUN TEST
if __name__ == "__main__":
    texts = load_texts()
    embeddings = create_embeddings(texts)
    index = build_index(embeddings)

    query = "family SUV with more seats"
    results = search(query, index, texts)

    print("\nRESULTS:\n")
    for r in results:
        print("-", r)